DELIMITER //

DROP TRIGGER IF EXISTS UPDATE_SONG_NO_AFTER_INSERT;
CREATE TRIGGER UPDATE_SONG_NO_AFTER_INSERT
AFTER INSERT ON SONG
FOR EACH ROW
BEGIN
    UPDATE ARTIST
	@@ -77,11 +77,37 @@ BEGIN
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
	@@ -90,6 +116,15 @@ BEGIN
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