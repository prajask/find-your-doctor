"""
Database Models

"""

from extensions import database

#Patient User Model Definition
class Patient(database.Model):
    id = database.Column( database.Integer, primary_key = True )
    first_name = database.Column( database.String(50) )
    last_name = database.Column( database.String(50) )
    email = database.Column( database.String(100), unique = True )
    phone_number = database.Column( database.BigInteger, unique = True )
    password_hash = database.Column( database.String(1024) )

    appointments = database.relationship("Doctor", secondary = "appointment", backref = "patient", lazy = "dynamic")

    def to_dict(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "password_hash": self.password_hash
        }

#Doctor User Model Definition
class Doctor(database.Model):
    id = database.Column( database.Integer, primary_key = True )
    government_id = database.Column( database.String(20), unique = True )
    first_name = database.Column( database.String(50) )
    last_name = database.Column( database.String(50) )
    email = database.Column( database.String(100), unique = True )
    phone_number = database.Column( database.BigInteger, unique = True )
    password_hash = database.Column( database.String(1024) )
    verified = database.Column( database.Boolean )

    appointments = database.relationship("Patient", secondary = "appointment", backref = "doctor", lazy = "dynamic")
    degrees = database.relationship("Degree", secondary = "doctor_degrees", backref = "doctor", lazy = "dynamic")

    def to_dict(self):
        return {
            "id": self.id,
            "government_id": self.government_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "password_hash": self.password_hash,
            "verified": self.verified
        }

#Degree Model Definition
class Degree(database.Model):
    id = database.Column( database.Integer, primary_key = True )
    name = database.Column( database.String(30) )

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

database.Table(
    "doctor_degrees",
    database.Column( "doctor", database.Integer, database.ForeignKey("doctor.id") ),
    database.Column( "degree", database.Integer, database.ForeignKey("degree.id") )
    )

#Appointment Model Definition
class Appointment(database.Model):
    id = database.Column( database.Integer, primary_key = True )
    patient = database.Column( database.Integer, database.ForeignKey("patient.id") )
    doctor = database.Column( database.Integer, database.ForeignKey("doctor.id") )
    time = database.Column( database.DateTime )
    status = database.Column( database.String(15) )
    has_report = database.Column( database.Boolean )

    def to_dict(self):
        return {
            "id": self.id,
            "patient": self.patient,
            "doctor": self.doctor,
            "time": self.time,
            "status": self.status,
            "has_report": self.has_report
        }

#Report Model Definition
class Report(database.Model):
    id = database.Column( database.Integer, primary_key = True )
    appointment = database.Column( database.Integer, database.ForeignKey("appointment.id") )
    red_blood_cell_count = database.Column( database.Integer )
    white_blood_cell_count = database.Column( database.Integer )
    sugar_level = database.Column( database.Integer )

    def to_dict(self):
        return {
            "id": self.id,
            "appointment": self.appointment,
            "red_blood_cell_count": self.red_blood_cell_count,
            "white_blood_cell_count": self.white_blood_cell_count,
            "sugar_level": self.sugar_level
        }