from flask import Blueprint, request
from api.models import User
from api.core import create_response, serialize_list, logger
from googlemaps import Client

main = Blueprint("main", __name__)  # initialize blueprint

gmaps = Client(key='AIzaSyAMA6Vw5X3pzhUxUPe_fPUrOXwVvpclxr0')
# function that is called when you visit /
@main.route("/create_user", methods=['POST'])
def create_user():
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself\
    code = request.args.get('code')
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    new_user = User(lat, lon, code)
    new_user.add_user()
    return create_response(status=201)


# function that is called when you visit /persons
@main.route("/rendezvous", methods=["GET"])
def rendezvous():
    code = request.args.get('code')
    users = User.query.filter(User.code==code)
    lats = [user.lat for user in users]
    lons = [user.lon for user in users]

    centr_lat = sum(lats) / len(lats)
    centr_lon = sum(lons) / len(lons)

    global gmaps
    response = gmaps.places_nearby(location=(centr_lat, centr_lon), rank_by='distance', type="store")
    name = response['results'][0]['name']
    loc = response['results'][0]['geometry']['location']
    lat, lon = loc['lat'], loc['lng']

    return create_response(data={"lat": lat, "lon": lon, "name": name})
