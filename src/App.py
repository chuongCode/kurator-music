import os
from flask import Flask, session, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

print("sqlite:///" + os.path.join(basedir, "create.sql"))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(basedir, "mydatabase.sql")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "abc123"

db = SQLAlchemy(app)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class Song(db.Model):
    __tablename__ = 'song'
    song_name = db.Column(db.String(255), primary_key=True)
    artist = db.Column(db.String(255), db.ForeignKey('artist.artist_name'))
    album = db.Column(db.String(255), db.ForeignKey('album.album_name'))
    date_modified = db.Column(db.Date)
    date_created = db.Column(db.Date)

    artist_rel = db.relationship('Artist', backref='songs')
    album_rel = db.relationship('Album', backref='songs')

class Artist(db.Model):
    __tablename__ = 'artist'
    artist_name = db.Column(db.String(255), primary_key=True)
    language = db.Column(db.String(255))
    sno = db.Column(db.Integer)
    ano = db.Column(db.Integer)

class Album(db.Model):
    __tablename__ = 'album'
    album_name = db.Column(db.String(255), primary_key=True)
    artist = db.Column(db.String(255), db.ForeignKey('artist.artist_name'))
    language = db.Column(db.String(255))
    year = db.Column(db.Integer)
    ano = db.Column(db.Integer)

    artist_rel = db.relationship('Artist', backref='albums')

class Language(db.Model):
    __tablename__ = 'language'
    language_name = db.Column(db.String(255), primary_key=True)
    sno = db.Column(db.Integer)

class FileInfo(db.Model):
    __tablename__ = 'file_info'
    file_name = db.Column(db.String(255), primary_key=True)
    file_type = db.Column(db.String(255))
    song = db.Column(db.String(255), db.ForeignKey('song.song_name'))
    artist = db.Column(db.String(255), db.ForeignKey('artist.artist_name'))
    album = db.Column(db.String(255), db.ForeignKey('album.album_name'))
    
    song_rel = db.relationship('Song', backref='file_info')
    artist_rel = db.relationship('Artist', backref='file_info')
    album_rel = db.relationship('Album', backref='file_info')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

class SongForm(FlaskForm):
    song_name = StringField("Song")
    artist = StringField("Artist")
    album = StringField("Album")
    submit = SubmitField("Submit")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# class DeleteForm(FlaskForm):
#     netid = StringField("Enter the NetID to remove: ", validators=[DataRequired()])
#     submit = SubmitField("Delete User")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.route("/", methods = ["GET", "POST"])
def index():
    all_songs = Song.query.all()
    print(all_songs[0].song_name)
    return render_template("index.html", songs = all_songs)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/admin_index", methods = ["GET", "POST"])
def admin_index():
    form = SongForm()
    if(form.validate_on_submit()):
        song_name = form.song_name.data
        artist = form.artist.data
        album = form.album.data
        print("The song details are" + song_name + artist + album)

        new_song = Song(song_name = song_name, artist = artist, album = album)
        db.session.add(new_song)
        db.session.commit()

        return redirect(url_for("index"))

    return render_template("admin_index.html", form = form)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
