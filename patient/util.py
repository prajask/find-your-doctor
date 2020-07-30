"""
Utility Functions for Patient Users

"""

from flask import session
from models import Patient, Doctor, Degree, Appointment, Report, database
from datetime import datetime, timedelta

def get_all_appointments(patient_id):
    appointments = list()

    for appointment in Appointment.query.filter_by( patient = patient_id ).all():
        appointments.append( get_appointment_information(appointment.id) )

    return appointments

def get_appointment_information(appointment_id):
    appointment = Appointment.query.filter_by( id = appointment_id ).first()
    appointment_information = appointment.to_dict()
    appointment_information["doctor"] = get_doctor_information( appointment_information["doctor"] )
    appointment_information["date"] = get_date_string( datetime.date( appointment_information["time"] ) )
    appointment_information["today"] = True if ( datetime.now().date() - datetime.date( appointment_information["time"] ) == timedelta(0) ) else False
    appointment_information["time"] = get_time_string( datetime.time( appointment_information["time"] ) )

    if appointment_information["has_report"]:
        appointment_information["report"] = get_appointment_report(appointment_information["id"])

    return appointment_information

def get_doctor_information(doctor_id):
    doctor = Doctor.query.filter_by( id = doctor_id ).first()
    doctor_information = doctor.to_dict()
    del doctor_information["password_hash"]

    return doctor_information

def get_date_string(date):
    if date.day < 10 and date.month < 10:
        return "0{} - 0{} - {}".format( date.day, date.month, date.year )

    elif date.day < 10:
        return "0{} - {} - {}".format( date.day, date.month, date.year )

    elif date.month < 10:
        return "{} - 0{} - {}".format( date.day, date.month, date.year )

    else:
        return "{} - {} - {}".format( date.day, date.month, date.year )

def get_time_string(time):
    if time.hour < 10 and time.minute < 10:
        return "0{} : 0{}".format( time.hour, time.minute )

    elif time.hour < 10:
        return "0{} : {}".format( time.hour, time.minute )

    elif time.minute < 10:
        return "{} : 0{}".format( time.hour, time.minute )
        
    else:
        return "{} : {}".format( time.hour, time.minute )

def get_appointment_report(appointment_id):
    report = Report.query.filter_by(appointment = appointment_id).first()

    if report:
        report_details = report.to_dict()
        report_details["report_status"] = True

        return report_details

    else:
        return False

def get_all_doctors():
    all_doctors = list()
    doctors = Doctor.query.filter_by( verified = True ).all()

    for doctor in doctors:
        doctor_information = doctor.to_dict()
        doctor_information["degrees"] = [ degree.name for degree in doctor.degrees.all() ]
        del doctor_information["password_hash"]
        all_doctors.append(doctor_information)

    return all_doctors

def book_appointment(doctor_id, appointment_information):
    date = appointment_information["date"].split('-')
    
    appointment = Appointment(
        patient = session["user"]["id"],
        doctor = doctor_id,
        time = datetime( int(date[0]), int(date[1]), int(date[2]), int(appointment_information["time"]), 0 ),
        status = "pending",
        has_report = True
    )

    database.session.add(appointment)

    database.session.commit()
