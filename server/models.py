from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4

db = SQLAlchemy()


def get_uuid():
    return uuid4().hex


class User(db.Model):
    __tablename__ = "user"
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, unique=True, default=get_uuid, primary_key=True)
    name = db.Column(db.Text, nullable=False)
    username = db.Column(db.Text, nullable=False, unique=True)
    email = db.Column(db.Text, unique=True, primary_key=True)
    role = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)


class JobSeeker(db.Model):
    __tablename__ = "jobseeker"
    __table_args__ = {'extend_existing': True}
    #jobseekerid = db.Column(db.Text, nullable=False, unique=True)
    jobseekername = db.Column(db.Text, nullable=False)
    qualifications = db.Column(db.Text, nullable=False)
    interests = db.Column(db.Text, nullable=False)
    chatbotresponse = db.Column(db.Text, nullable=False)
    jobseekermail = db.Column(db.Text, unique=True, primary_key=True)
    # classid = db.Column(db.Text, nullable=False)


class Company(db.Model):
    __tablename__ = "company"
    __table_args__ = {'extend_existing': True}
    #companyid = db.Column(db.Text, nullable=False, unique=True)
    # classid = db.Column(db.Text, nullable=False)
    companyname = db.Column(db.Text, nullable=False)
    post = db.Column(db.Text, nullable=False)
    jobdescription = db.Column(db.Text, nullable=False)
    companymail = db.Column(db.Text, unique=True, primary_key=True)

