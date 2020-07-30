"""
Patient User Routes

"""

from flask import Blueprint, session, render_template, url_for, redirect, request
from patient import util

patient = Blueprint("patient", __name__, url_prefix = "/patient", template_folder = "templates")

@patient.route('/')
def index():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect(url_for("auth.login"))
    
    else:
        booking_successful = True if ( "booking_successful" in session and session["booking_successful"] ) else False
        session["booking_successful"] = False

        return render_template("patient/index.html", appointments = util.get_all_appointments(session["user"]["id"]), booking_successful = booking_successful)

@patient.route("/book_appointment/<string:doctor_id>", methods = ["POST"])
def book_appointment(doctor_id):
    if "logged_in" not in session or not session["logged_in"]:
        return redirect(url_for("auth.login"))

    else:
        util.book_appointment(doctor_id, request.form)
        session["booking_successful"] = True

        return redirect(url_for("patient.index"))

@patient.route("/appointment/<string:appointment_id>")
def appointment(appointment_id):
    if "logged_in" not in session or not session["logged_in"]:
        return redirect(url_for("auth.login"))

    else:
        if appointment_id == "new_appointment":
            return render_template("patient/new_appointment.html", doctors = util.get_all_doctors())
        
        else:
            return render_template("patient/appointment.html", appointment_information = util.get_appointment_information(appointment_id))