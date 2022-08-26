"""
Doctor User Routes

"""

from flask import Blueprint, session, render_template, redirect, url_for, request
from doctor import util

doctor = Blueprint("doctor", __name__, url_prefix = "/doctor", template_folder = "templates")

@doctor.route('/')
def index():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect( url_for( "auth.login" ) )

    else:
        if not session["user"]["verified"]:
            return render_template("doctor/unverified.html")

        else:
            return render_template("doctor/index.html", appointments = util.get_all_appointments( session["user"]["id"] ))

@doctor.route("/appointment/<string:appointment_id>")
def appointment(appointment_id):
    if "logged_in" not in session or not session["logged_in"]:
        return redirect( url_for( "auth.login" ) )
    
    else:
        return render_template("doctor/appointment.html", appointment_information = util.get_appointment_information(appointment_id))

@doctor.route("/patient_history/<string:patient_id>")
def patient_history(patient_id):
    if "logged_in" not in session or not session["logged_in"]:
        return redirect( url_for( "auth.login" ) )

    else:
        return render_template("doctor/patient_history.html", patient_history = util.get_patient_history(patient_id))

@doctor.route("/complete_appointment/<string:appointment_id>/<string:action>", methods = ["POST"])
def complete_appointment(appointment_id, action):
    if "logged_in" not in session or not session["logged_in"]:
        return redirect( url_for( "auth.login" ) )

    else:
        util.complete_appointment(appointment_id, action, request.form)

        return redirect( url_for( "doctor.appointment", appointment_id = appointment_id ) )

@doctor.route('/profile')
def profile():
    if "logged_in" not in session or not session["logged_in"]:
        return redirect( url_for( "auth.login" ) )
    
    else:
        return render_template("doctor/profile.html")