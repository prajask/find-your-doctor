"""
Utility Functions for Doctor Users

"""


from flask import session
from models import Patient, Doctor, Degree, Appointment, Report, database
from datetime import datetime, timedelta

def get_all_appointments(id):
    appointments = list()

    for appointment in Appointment.query.filter( Appointment.doctor == id, Appointment.status != "cancelled" ).all():
        appointments.append( get_appointment_information(appointment.id) )

    return appointments

def get_appointment_information(appointment_id):
    appointment = Appointment.query.filter_by( id = appointment_id ).first()
    appointment_information = appointment.to_dict()
    appointment_information["patient"] = get_patient_information( appointment_information["patient"] )
    appointment_information["date"] = get_date_string( datetime.date( appointment_information["time"] ) )
    appointment_information["today"] = True if ( datetime.now().date() - datetime.date( appointment_information["time"] ) == timedelta(0) ) else False
    appointment_information["time"] = get_time_string( datetime.time( appointment_information["time"] ) )

    if appointment_information["has_report"]:
        appointment_information["report"] = get_appointment_report(appointment_information["id"])

    return appointment_information


def get_patient_information(patient_id):
    patient = Patient.query.filter_by( id = patient_id ).first()
    patient_information = patient.to_dict()
    del patient_information["password_hash"]

    return patient_information

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

def get_patient_history(patient_id):
    patient_history = list()
    appointments = Appointment.query.filter_by( patient = patient_id ).all()
    
    for appointment in appointments:
        appointment_information = get_appointment_information(appointment.id)
        appointment_information["doctor"] = get_doctor_information(appointment_information["doctor"])
        patient_history.append(appointment_information) if appointment_information["status"] == "completed" else False

    return patient_history

def get_doctor_information(doctor_id):
    doctor = Doctor.query.filter_by( id = doctor_id ).first()
    doctor_information = doctor.to_dict()
    del doctor_information["password_hash"]

    return doctor_information

def complete_appointment(appointment_id, action, report):
    appointment = Appointment.query.filter_by( id = appointment_id ).first()

    if action == "update":
        update_report(appointment_id, report)

    else:
        if action == "complete_now":
            add_report(appointment_id, report)

        elif action == "no_report":
            appointment.has_report = False

        appointment.status = "completed"
        database.session.commit()

def update_report(appointment_id, report_details):
    report = Report.query.filter_by( appointment = appointment_id ).first()

    if report:
        report.red_blood_cell_count = report_details["red_blood_cell_count"]
        report.white_blood_cell_count = report_details["white_blood_cell_count"]
        report.sugar_level = report_details["sugar_level"]
        database.session.commit()

    else:
        add_report(appointment_id, report_details)

def add_report(appointment_id, report):
    report = Report(
        appointment = appointment_id,
        red_blood_cell_count = report["red_blood_cell_count"],
        white_blood_cell_count = report["white_blood_cell_count"],
        sugar_level = report["sugar_level"]
    )

    database.session.add(report)
    database.session.commit()