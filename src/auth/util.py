"""
Authentication Utility Functions

"""

from flask import session
from models import Patient, Doctor, Degree, database
import hashlib, binascii
from config import SECRET_KEY

def get_degrees():
    return [ degree.to_dict() for degree in Degree.query.all() ]

def register_user(user_data):
    registration_details = {
        "registration_successful": True,
    }

    if email_already_registered(user_data["email"]):
        registration_details["registration_successful"] = False
        registration_details["error"] = "email_error"

        return registration_details
    
    if phone_number_already_registered(user_data["phone_number"]):
        registration_details["registration_successful"] = False
        registration_details["error"] = "phone_number_error"

        return registration_details

    if government_id_already_registered(user_data["government_id"]):
        registration_details["registration_successful"] = False
        registration_details["error"] = "government_id_error"

        return registration_details

    user = create_user(user_data)
    
    if user:
        registration_details["user"] = user.to_dict()

    else:
        registration_details["registration_successful"] = False
        registration_details["error"] = "Something Went Wrong. Try Again."

    return registration_details

def email_already_registered(email):
    patient_exists = Patient.query.filter_by(email = email).first()
    doctor_exists = Doctor.query.filter_by(email = email).first()

    return True if ( patient_exists or doctor_exists ) else False

def phone_number_already_registered(phone_number):
    patient_exists = Patient.query.filter_by(phone_number = phone_number).first()
    doctor_exists = Doctor.query.filter_by(phone_number = phone_number).first()

    return True if ( patient_exists or doctor_exists ) else False

def government_id_already_registered(government_id):
    doctor_exists = Doctor.query.filter_by(government_id = government_id).first()

    return True if doctor_exists else False

def create_user(user_data):
    user = create_patient(user_data) if user_data["user_type"] == "patient" else create_doctor(user_data)
    database.session.add(user)
    database.session.commit()

    return user

def create_patient(user_data):
    user = Patient(
            first_name = user_data["first_name"],
            last_name = user_data["last_name"],
            email = user_data["email"],
            phone_number = user_data["phone_number"],
            password_hash = create_password_hash( user_data["password"] )
        )

    return user

def create_doctor(user_data):
    user = Doctor(
            government_id = user_data["government_id"],
            first_name = user_data["first_name"],
            last_name = user_data["last_name"],
            email = user_data["email"],
            phone_number = user_data["phone_number"],
            password_hash = create_password_hash( user_data["password"] ),
            verified = False
        )
    add_doctor_degrees( user, user_data.getlist("degree") )

    return user

def add_doctor_degrees(doctor, degrees):
    for degree in degrees:
        current_degree = Degree.query.filter_by( id = int(degree) ).first()
        current_degree.doctor.append(doctor)

def create_password_hash(password):
    return binascii.hexlify( hashlib.pbkdf2_hmac( "sha256",  password.encode(), SECRET_KEY.encode(), 5000) ).decode()

def verify_credentials(user_credentials):
    user = get_user(user_credentials["email"])

    if user and verify_password( user_credentials["password"], user["password_hash"] ):
        create_session(user)
        return True
    
    else:
        return False

def get_user(email):
    patient = True
    user = Patient.query.filter_by( email = email ).first()
    
    if not user:
        patient = False
        user = Doctor.query.filter_by( email = email ).first()

    if user:
        user = user.to_dict()
        user["user_type"] = "patient" if patient else "doctor"

        return user
    
    return False

def verify_password(password, password_hash):
    return binascii.hexlify( hashlib.pbkdf2_hmac( "sha256",  password.encode(), SECRET_KEY.encode(), 5000) ).decode() == password_hash

def create_session(user_data):
    session["logged_in"] = True
    session["user"] = user_data
    del session["user"]["password_hash"]

def update_password(user_credentails):
    updation_details = dict()

    user = get_user(user_credentails["email"])

    if not user:
        updation_details["status"] = False
        updation_details["error"] = "Invalid Email ID"
    
    else:
        user = Patient.query.filter_by( id = user["id"] ).first() if user["user_type"] == "patient" else Doctor.query.filter_by( id = user["id"] ).first()
        user.password_hash = create_password_hash(user_credentails["password"])
        database.session.commit()
        updation_details["status"] = True

    return updation_details