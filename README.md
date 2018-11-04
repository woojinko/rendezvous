# Rendezvous API

API for Rendezvous app built for Cal Hacks 5.0 (2018).

## Live Deploy

https://rendezvous-api.herokuapp.com/

## Endpoints

* POST create_user
  * param: code (int)
    * The user generated 6-digit code for their rendezvous group
  * param: lat (float)
    * The user's latitude
  * param: lon (float)
    * The user's longitude
* GET rendezvous, party_size, get_dest
  * param: code (int)
    * The 6-digit code used to identify the user's group
* GET locate_party
  * param: code (int)
    * The 6-digit code used to identify the user's group
  * param: user_id (int)
    * The id of the user who sent the request

## Testing with Postman

Load both collections into [Postman]() and run Rendezvous 1 and then 2. The requests in Rendezvous 1 are not idempotent so you must only run Rendezvous 1 once. Make absolutely sure to change the code field before running.

## Built With

* [Flask](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Heroku](http://flask.pocoo.org/) - Deployment
* [Flask Boilerplate](https://github.com/tko22/flask-boilerplate) - Boilerplate used

## Authors

* **Avneesh Mehta**
* **Woojin Ko**
* **Bayan Alizadeh**
* **Newman Hu**

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* All members of the team
* Inspiration
* Cal Hacks 5.0 sponsors and mentors
