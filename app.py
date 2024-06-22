from flask import Flask
from Api.user_controller import user_controller
from Api.city_controller import city_control
from Api.country_city_controller import country_city_controller
from Api.country_controller import coutry_controller
from Api.amenity_controller import amenity_controller
from Api.place_controller import place_controller
from Api.review_controller import review_controller

app = Flask(__name__)

# app.register_blueprint(user_controller)
# app.register_blueprint(country_city_controller)
# app.register_blueprint(coutry_controller)
app.register_blueprint(city_control)
# app.register_blueprint(amenity_controller)
# app.register_blueprint(place_controller)
# app.register_blueprint(review_controller)

@app.route('/')
def hello():
    return "Welcome to Hbnb part 1"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)