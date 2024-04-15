CREATE TABLE IF NOT EXISTS LANGUAGE (
    Language_name VARCHAR(32),
    Song_no INT,
    PRIMARY KEY (Language_name)
);

CREATE TABLE IF NOT EXISTS ARTIST (
    Artist_name VARCHAR(64),
    Language_name VARCHAR(32),
    Song_no INT,
    Album_no INT,
    PRIMARY KEY (Artist_name),
    FOREIGN KEY (Language_name) REFERENCES LANGUAGE(Language_name) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS ALBUM (
    Album_name VARCHAR(128),
    Artist_name VARCHAR(64),
    Language_name VARCHAR(32),
    Year INT,
    Song_no INT,
    PRIMARY KEY (Album_name, Artist_name),
    FOREIGN KEY (Artist_name) REFERENCES ARTIST(Artist_name) ON DELETE CASCADE,
    FOREIGN KEY (Language_name) REFERENCES LANGUAGE(Language_name) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS SONG (
    Song_name VARCHAR(128),
    Artist_name VARCHAR(64),
    Album_name VARCHAR(128),
    Date_modified DATE,
    Date_created DATE,
    PRIMARY KEY (Song_name),
    FOREIGN KEY (Artist_name) REFERENCES ARTIST(Artist_name) ON DELETE CASCADE,
    FOREIGN KEY (Album_name) REFERENCES ALBUM(Album_name) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS FILE (
    File_name VARCHAR(128),
    File_type VARCHAR(4),
    Song_name VARCHAR(128) NOT NULL,
    Artist_name VARCHAR(64),
    Album_name VARCHAR(128),
    PRIMARY KEY (File_name),
    FOREIGN KEY (Song_name) REFERENCES SONG(Song_name) ON DELETE CASCADE,
    FOREIGN KEY (Artist_name) REFERENCES ARTIST(Artist_name) ON DELETE CASCADE,
    FOREIGN KEY (Album_name) REFERENCES ALBUM(Album_name) ON DELETE CASCADE
);

DELIMITER //

DROP TRIGGER IF EXISTS UPDATE_SONG_NO_AFTER_INSERT;
CREATE TRIGGER UPDATE_SONG_NO_AFTER_INSERT
AFTER INSERT ON SONG
FOR EACH ROW
BEGIN
    UPDATE ARTIST
    SET Song_no = (SELECT COUNT(*) FROM SONG WHERE ARTIST.Artist_name = SONG.Artist_name)
    WHERE ARTIST.Artist_name = NEW.Artist_name;

    UPDATE ALBUM
    SET Song_no = (SELECT COUNT(*) FROM SONG WHERE ALBUM.Album_name = SONG.Album_name)
    WHERE ALBUM.Album_name = NEW.Album_name;

    UPDATE LANGUAGE
    SET Song_no = (
        SELECT COUNT(*) 
        FROM SONG
        INNER JOIN ALBUM ON ALBUM.Album_name = SONG.Album_name 
        WHERE ALBUM.Language_name = LANGUAGE.Language_name
    )
    WHERE LANGUAGE.Language_name = (
        SELECT ALBUM.Language_name 
        FROM ALBUM 
        WHERE ALBUM.Album_name = NEW.Album_name
    );
END;
//

DROP TRIGGER IF EXISTS UPDATE_SONG_NO_AFTER_DELETE;
CREATE TRIGGER UPDATE_SONG_NO_AFTER_DELETE
AFTER DELETE ON SONG
FOR EACH ROW
BEGIN
    UPDATE ARTIST
    SET Song_no = (SELECT COUNT(*) FROM SONG WHERE ARTIST.Artist_name = SONG.Artist_name)
    WHERE ARTIST.Artist_name = OLD.Artist_name;

    UPDATE ALBUM
    SET Song_no = (SELECT COUNT(*) FROM SONG WHERE ALBUM.Album_name = SONG.Album_name)
    WHERE ALBUM.Album_name = OLD.Album_name;

    UPDATE LANGUAGE
    SET Song_no = (
        SELECT COUNT(*) 
        FROM SONG
        INNER JOIN ALBUM ON ALBUM.Album_name = SONG.Album_name 
        WHERE ALBUM.Language_name = LANGUAGE.Language_name
    )
    WHERE LANGUAGE.Language_name = (
        SELECT ALBUM.Language_name 
        FROM ALBUM 
        WHERE ALBUM.Album_name = OLD.Album_name
    );
END;
//

DROP TRIGGER IF EXISTS UPDATE_ALBUM_NO_AFTER_INSERT;
CREATE TRIGGER UPDATE_ALBUM_NO_AFTER_INSERT
AFTER INSERT ON ALBUM
FOR EACH ROW
BEGIN
    UPDATE ARTIST
    SET Album_no = (SELECT COUNT(*) FROM ALBUM WHERE ARTIST.Artist_name = ALBUM.Artist_name)
    WHERE ARTIST.Artist_name = NEW.Artist_name;
END;
//

DROP TRIGGER IF EXISTS UPDATE_ALBUM_NO_AFTER_DELETE;
CREATE TRIGGER UPDATE_ALBUM_NO_AFTER_DELETE
AFTER DELETE ON ALBUM
FOR EACH ROW
BEGIN
    UPDATE ARTIST
    SET Album_no = (SELECT COUNT(*) FROM ALBUM WHERE ARTIST.Artist_name = ALBUM.Artist_name)
    WHERE ARTIST.Artist_name = OLD.Artist_name;
END;
//

DELIMITER ;
