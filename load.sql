LOAD DATA INFILE '/home/stsegai/language_entries.csv'
INTO TABLE LANGUAGE
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/stsegai/artist_entries.csv'
INTO TABLE ARTIST
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/stsegai/album_entries.csv'
INTO TABLE ALBUM
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/stsegai/song_entries.csv'
INTO TABLE SONG
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';

LOAD DATA INFILE '/home/stsegai/file_entries.csv'
INTO TABLE FILE
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n';