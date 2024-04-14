import os
from flask import Flask, session, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired

from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "data.sqlite")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["SECRET_KEY"] = "abc123"
# UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'images')

# print(UPLOAD_FOLDER)
# app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# db = SQLAlchemy(app)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class Song(db.Model):
#     __tablename__ = 'song'
#     song_name = db.Column(db.String(255), primary_key=True)
#     youtube_link = db.Column(db.String(255), primary_key=True)
#     artist = db.Column(db.String(255), db.ForeignKey('artist.artist_name'))
#     album = db.Column(db.String(255), db.ForeignKey('album.album_name'))
#     date_modified = db.Column(db.Date)
#     date_created = db.Column(db.Date)

#     artist_rel = db.relationship('Artist', backref='songs')
#     album_rel = db.relationship('Album', backref='songs')

# class Artist(db.Model):
#     __tablename__ = 'artist'
#     artist_name = db.Column(db.String(255), primary_key=True)
#     language = db.Column(db.String(255))
#     sno = db.Column(db.Integer)
#     ano = db.Column(db.Integer)

# class Album(db.Model):
#     __tablename__ = 'album'
#     album_name = db.Column(db.String(255), primary_key=True)
#     artist = db.Column(db.String(255), db.ForeignKey('artist.artist_name'))
#     language = db.Column(db.String(255))
#     year = db.Column(db.Integer)
#     ano = db.Column(db.Integer)

#     artist_rel = db.relationship('Artist', backref='albums')

# class Language(db.Model):
#     __tablename__ = 'language'
#     language_name = db.Column(db.String(255), primary_key=True)
#     sno = db.Column(db.Integer)

# class FileInfo(db.Model):
#     __tablename__ = 'file_info'
#     file_name = db.Column(db.String(255), primary_key=True)
#     file_type = db.Column(db.String(255))
#     song = db.Column(db.String(255), db.ForeignKey('song.song_name'))
#     artist = db.Column(db.String(255), db.ForeignKey('artist.artist_name'))
#     album = db.Column(db.String(255), db.ForeignKey('album.album_name'))
    
#     song_rel = db.relationship('Song', backref='file_info')
#     artist_rel = db.relationship('Artist', backref='file_info')
#     album_rel = db.relationship('Album', backref='file_info')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class UserForm(FlaskForm):
#     netid = StringField("NetID: ", validators=[DataRequired()])
#     fname = StringField("First name: ", validators=[DataRequired()])
#     lname = StringField("Last name: ", validators=[DataRequired()])
#     email = StringField("Email: ", validators=[DataRequired()])
#     password = PasswordField("Password: ", validators=[DataRequired()])
#     isMentor  = BooleanField("Would you like to be a mentor?", validators=[])
#     submit = SubmitField("Continue")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class DeleteForm(FlaskForm):
#     netid = StringField("Enter the NetID to remove: ", validators=[DataRequired()])
#     submit = SubmitField("Delete User")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/admin_index")
def admin_index():
    return render_template("admin_index.html")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# def createUser(netid, fname, lname, email, pw, isMentor, pfp):
#     user = User(netid = netid, firstname = fname, lastname = lname, email = email, password = pw, isMentor = isMentor, pfp=pfp)
#     db.session.add(user)
#     db.session.commit()

# def deleteUser(netid):
#     user = User.query.filter_by(netid = netid).first()
#     if(user != None):
#         db.session.delete(user)
#         db.session.commit()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# @app.before_first_request
# def create_tables():
#     db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
