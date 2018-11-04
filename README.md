# Rendezvous API

API for Rendezvous app built for Cal Hacks 5.0 (2018).

## Endpoints

* create_user
  * param: code (int)
    * The user generated 6-digit code for their rendezvous group
  * param: lat (float)
    * The user's latitude (float
  * param: lon (float)
    * The user's longitude
* rendezvous
  * param: code (int)
    * The 6-digit code used to identify the user's group 

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

* @tko22
* Inspiration
* Cal Hacks 5.0 sponsors and mentors
