CREATE TABLE SONG (
    Song_name VARCHAR(255),
    Youtube_link VARCHAR(255),
    Artist VARCHAR(255),
    Album VARCHAR(255),
    Date_modified DATE,
    Date_created DATE,
    PRIMARY KEY (Song_name, Youtube_link),
    FOREIGN KEY (Artist) REFERENCES ARTIST(Artist_name),
    FOREIGN KEY (Album) REFERENCES ALBUM(Album_name)
);

CREATE TABLE ARTIST (
    Artist_name VARCHAR(255) PRIMARY KEY,
    Language VARCHAR(255),
    Sno INT,
    Ano INT
);

CREATE TABLE ALBUM (
    Album_name VARCHAR(255),
    Artist VARCHAR(255),
    Language VARCHAR(255),
    Year INT,
    Ano INT,
    PRIMARY KEY (Album_name, Artist),
    FOREIGN KEY (Artist) REFERENCES ARTIST(Artist_name)
);

CREATE TABLE LANGUAGE (
    Language_name VARCHAR(255) PRIMARY KEY,
    Sno INT
);

CREATE TABLE FILE_INFO (
    File_name VARCHAR(255) PRIMARY KEY,
    File_type VARCHAR(255),
    Song VARCHAR(255),
    Artist VARCHAR(255),
    Album VARCHAR(255),
    FOREIGN KEY (Song, Artist, Album) REFERENCES SONG(Song_name, Artist, Album),
    FOREIGN KEY (Artist) REFERENCES ARTIST(Artist_name),
    FOREIGN KEY (Album) REFERENCES ALBUM(Album_name)
);