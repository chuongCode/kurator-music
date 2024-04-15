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

    def modify(self, artist, album):
        self.artist = artist
        self.album = album
        db.session.commit()

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

@app.route("/deleteSong/<song_name>", methods=["POST"])
def deleteSong(song_name):
    song = Song.query.filter_by(song_name = song_name).first()
    if(song != None):
        db.session.delete(song)
        db.session.commit()
    return render_template("admin_index.html", form = SongForm(), songs = Song.query)

@app.route("/modifySong/<song_name>", methods=["POST"])
def modifySong(song_name):
    song = Song.query.filter_by(song_name=song_name).first()
    if song is not None:
        artist = request.form.get('artist')
        album = request.form.get('album')
        song.modify(artist, album)
    return redirect(url_for('admin_index'))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.route("/", methods = ["GET", "POST"])
def index():
    all_songs = Song.query

    search_term_song = request.args.get('search_song', '')
    search_term_artist = request.args.get('search_artist', '')
    search_term_album = request.args.get('search_album', '')
    search_term_file = request.args.get('search_file', '')
    if search_term_song:
        all_songs = all_songs.filter(Song.song_name.ilike(f"%{search_term_song}%"))
    if search_term_artist:
        all_songs = all_songs.filter(Song.artist.ilike(f"%{search_term_artist}%"))
    if search_term_album:
        all_songs = all_songs.filter(Song.album.ilike(f"%{search_term_album}%"))
    if search_term_file:
        all_songs = all_songs.filter(Song.file.ilike(f"%{search_term_file}%"))

    return render_template("index.html", songs = all_songs)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/admin_index", methods = ["GET", "POST"])
def admin_index():
    all_songs = Song.query
    form = SongForm()

    search_term_song = request.args.get('search_song', '')
    search_term_artist = request.args.get('search_artist', '')
    search_term_album = request.args.get('search_album', '')
    search_term_file = request.args.get('search_file', '')
    if search_term_song:
        print("AAA")
        all_songs = all_songs.filter(Song.song_name.ilike(f"%{search_term_song}%"))
    if search_term_artist:
        print("BBB")
        all_songs = all_songs.filter(Song.artist.ilike(f"%{search_term_artist}%"))
    if search_term_album:
        print("CCC")
        all_songs = all_songs.filter(Song.album.ilike(f"%{search_term_album}%"))
    if search_term_file:
        print("DDD")
        all_songs = all_songs.filter(Song.file.ilike(f"%{search_term_file}%"))

    if(form.validate_on_submit()):
        song_name = form.song_name.data
        artist = form.artist.data
        album = form.album.data

        new_song = Song(song_name = song_name, artist = artist, album = album)
        db.session.add(new_song)
        db.session.commit()

        return redirect(url_for("admin_index"))

    return render_template("admin_index.html", form = form, songs = all_songs)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
