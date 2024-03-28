# from __init__ import app

# if __name__ == '__main__':
# 	app.run(debug=True)
from flask import Flask, request, jsonify, session
from flask_bcrypt import Bcrypt  # pip install Flask-Bcrypt = https://pypi.org/project/Flask-Bcrypt/
from flask_cors import CORS, cross_origin  # ModuleNotFoundError: No module named 'flask_cors' = pip install Flask-Cors
from models import db, User, JobSeeker, Company
from werkzeug.utils import secure_filename
import os
from flask import send_file
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from flask import request, jsonify

import subprocess
import sqlite3

app = Flask(__name__)

mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'

app.config['SECRET_KEY'] = 'jobadvisor-portal-app'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobadv.db'

# SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_ECHO = True

bcrypt = Bcrypt(app)
CORS(app, supports_credentials=True)
db.init_app(app)


# with app.app_context():
#     db.create_all()

@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/signup", methods=["POST"])
def signup():
    print(request.data)
    name = request.json["name"]
    username = request.json["username"]
    email = request.json["email"]
    role = request.json["role"]
    password = request.json["password"]

    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        return jsonify({"error": "Email already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(name=name, username=username, email=email, role=role, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    # Check if the user is a jobseeker
    if role == 'jobseeker':
        # Create a new job seeker entry
        new_jobseeker = JobSeeker(jobseekername=name, jobseekermail=email)
        # new_jobseeker = jobseeker(jobseekerid=rollid, jobseekername=name, jobseekermail=email)
        db.session.add(new_jobseeker)
        db.session.commit()

        # Check if the user is a company
    if role == 'company':
        # Create a new company entry
        new_company = Company(companyname=name, companymail=email)
         #new_company = Company(companyname=name,post=email,jobdescription=email, companymail=email)
        db.session.add(new_company)
        db.session.commit()


    session["user_id"] = new_user.id
    return jsonify({
        "id": new_user.id,
        # "user_id": new_user.id,
        "email": new_user.email
    })


# @app.route("/companylogin", methods=["POST"])
# def login_company():
#     email = request.json["email"]
#     password = request.json["password"]
#
#     user = User.query.filter_by(email=email).first()
#
#     if user is None:
#         return jsonify({"error": "Unauthorized Access"}), 401
#
#     if not bcrypt.check_password_hash(user.password, password):
#         return jsonify({"error": "Unauthorized"}), 401
#
#     session["user_id"] = user.id
#
#     return jsonify({
#         "id": user.id,
#         "email": user.email,
#         # "classid": user.classid
#     })

@app.route("/login", methods=["POST"])   #jobseekerlogin
def login():
    email = request.json["email"]
    password = request.json["password"]

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({"error": "Unauthorized Access"}), 401

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    session["user_id"] = user.id

    return jsonify({
        "id": user.id,
        "email": user.email,
        # "classid": user.classid
    })






# if __name__ == '__main__':
# #     if len(sys.argv) < 2:
# #         print('Please provide the classid as a command-line argument.')
# #         sys.exit(1)
# #
#     classid = sys.argv[1]
#     process_data(classid)




# @app.route('/logout/<int:user_id>', methods=["POST"])
@app.route('/logout', methods=["POST"])
# def logout(user_id):
def logout():
    # if "user_id" not in session or session["user_id"] != user_id:
    #     return jsonify({"error": "Unauthorized Access"}), 401

    session.clear()
    return jsonify({"message": "Logged out successfully"})


if __name__ == "__main__":
    app.run(debug=True)