"""
application: Find Your Doctor

author: Prajas Kadepurkar

"""

from flask import Flask, Blueprint

app = Flask(__name__)
app.config.from_pyfile("config.py")

#Importing and Initializing Extensions
from extensions import database
database.init_app(app)

#Importing models to create Database Tables
import models

#Importing and Registering Blueprints
from auth.routes import auth
app.register_blueprint(auth)

from patient.routes import patient
app.register_blueprint(patient)

from doctor.routes import doctor
app.register_blueprint(doctor)

#Run server
app.app_context().push()

if __name__ == "__main__":
    app.run(host="0.0.0.0")
