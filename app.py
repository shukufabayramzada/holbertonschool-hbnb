from flask import Flask
from Api.amenity_controller import amenity_controller

app = Flask(__name__)

app.register_blueprint(amenity_controller)

app = Flask(__name__)

@app.route('/')
def hello():
    return "Welcome to Hbnb project created by legends"

if __name__ == '__main__':
    app.run(host='localhost', port=8081, debug=True)