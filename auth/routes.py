"""
Authentication Routes

"""

from flask import Blueprint, session, render_template, url_for, redirect, request
from auth import util

auth = Blueprint("auth", __name__, template_folder = "templates")

@auth.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    
    return response

@auth.route('/', methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        user = util.verify_credentials(request.form)

        return redirect( url_for( "{}.index".format( session["user"]["user_type"] ) ) ) if user else render_template("auth/login.html", error = True)

    else:
        if "logged_in" in session and session["logged_in"]:
            return redirect( url_for( "{}.index".format( session["user"]["user_type"] ) ) )
        
        else:
            return render_template("auth/login.html")

@auth.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        registration_details = util.register_user(request.form)

        if registration_details["registration_successful"]:
            util.create_session( registration_details["user"] )

            return redirect( url_for ( "{}.index".format( request.form["user_type"] ) ) )

        else:
            return render_template("auth/register.html", degrees = util.get_degrees(), error = registration_details["error"])
    
    else:
        return render_template("auth/register.html", degrees = util.get_degrees())

@auth.route("/update_password", methods = ["GET", "POST"])
def update_password():
    if request.method == "POST":
        result = util.update_password(request.form)

        if result["status"]:
            session.clear()

            return render_template("auth/update_password.html", successful = True)

        else:
            return render_template("auth/update_password.html", error = result["error"])
    
    else:
        return render_template("auth/update_password.html")

@auth.route("/logout")
def logout():
    session.clear()
    
    return redirect("/")