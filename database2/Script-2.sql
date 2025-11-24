CREATE TABLE IF NOT EXISTS Jenre_list (
id_jenre SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artist_list (
id_artist SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Genre_artist(
id_jenre INTEGER REFERENCES Jenre_list (id_jenre),
id_artist INTEGER REFERENCES Artist_list (id_artist),
CONSTRAINT pk PRIMARY KEY (id_jenre, id_artist)
);

CREATE TABLE IF NOT EXISTS Album_list (
id_album SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
YEAR VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Artist_album (
id_artist INTEGER REFERENCES Artist_list (id_artist),
id_album INTEGER REFERENCES Album_list (id_album)
);

CREATE TABLE IF NOT EXISTS Track_list (
id_track SERIAL PRIMARY KEY,
id_album INTEGER NOT NULL REFERENCES Album_list (id_album),
name VARCHAR(120) NOT NULL,
time VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Collection_list (
id_collection SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
YEAR VARCHAR(60) NOT NULL
);

CREATE TABLE IF NOT EXISTS Collection_track (
id_collection INTEGER REFERENCES Collection_list (id_collection),
id_track INTEGER REFERENCES Track_list (id_track)
);
