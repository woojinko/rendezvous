from flask import Blueprint, request
from api.models import User, Destination
from api.core import create_response, serialize_list, logger
from googlemaps import Client
import os

main = Blueprint("main", __name__)  # initialize blueprint

gmaps = Client(key=os.environ.get('API_KEY'))

# called to create a new user and join a party_size
# params: code, lat, lon
@main.route("/create_user", methods=['POST'])
def create_user():
    code = request.args.get('code')
    lat = request.args.get('lat')
    lon = request.args.get('lon')

    new_user = User(lat, lon, code)
    new_user.add_user()
    print(str(new_user.id))
    return create_response(data={'user_id': str(new_user.id)}, status=201)

# called to initiate rendezvous calculation
# returns the best location for meetup
# params: code
@main.route("/rendezvous", methods=["GET"])
def rendezvous():
    code = request.args.get('code')
    dest = Destination.query.filter(Destination.code==code).all()
    if not dest:
        users = User.query.filter(User.code==code)
        lats = [user.lat for user in users]
        lons = [user.lon for user in users]

        centr_lat = sum(lats) / len(lats)
        centr_lon = sum(lons) / len(lons)

        global gmaps
        response = gmaps.places_nearby(location=(centr_lat, centr_lon), rank_by='distance', type="store")
        loc = response['results'][0]['geometry']['location']
        lat, lon = loc['lat'], loc['lng']

        dest = Destination(lat, lon, code)
        dest.add_dest()

        return create_response(data={"lat": lat, "lon": lon})
    elif len(dest) == 1:
        dest = dest[0]
        return create_response(data={"lat": dest.lat, "lon": dest.lon})
    else:
        return create_response(status=500)

# returns the party_size size for a given code
# params: code
@main.route("/party_size", methods=["GET"])
def party_size():
    code = request.args.get('code')
    users = User.query.filter(User.code==code).all()

    size = len(users)

    return create_response(data={"size": size})

# get the Destination again when clients request
# used to respond when clients request destination after rendezvous begins
# params: code
@main.route("/get_dest", methods=["GET"])
def get_dest():
    code = request.args.get('code')
    dest = Destination.query.filter(Destination.code==code).all()
    length = len(dest)
    if length == 0:
        return create_response(status=204)
    elif length == 1:
        dest = dest[0]
        return create_response(data={"lat": dest.lat, "lon": dest.lon})
    else:
        return create_response(status=500)

# returns the location of all other party members
# used to update live location on every Client
# params: code, user_id
@main.route("/locate_party", methods=["GET"])
def locate_party():
    code = request.args.get('code')
    user_id = request.args.get('user_id')

    users = User.query.filter((User.code==code) & (User.id != user_id))

    data = dict()
    for user in users:
        data.update({str(user.id): {"lat": user.lat, "lon": user.lon}})

    return create_response(data=data)
