CREATE TABLE IF NOT EXISTS Genre_list (
id_genre SERIAL PRIMARY KEY,
name_genre VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Artist_list (
id_artist SERIAL PRIMARY KEY,
name_artist VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Genre_artist(
id_genre INTEGER REFERENCES Genre_list (id_genre),
id_artist INTEGER REFERENCES Artist_list (id_artist),
constraint pk_Genre_artist PRIMARY KEY (id_genre, id_artist)
);

CREATE TABLE IF NOT EXISTS Album_list (
id_album SERIAL PRIMARY KEY,
name_album VARCHAR(60) NOT NULL UNIQUE,
year_album INTEGER CHECK (year_album > 2000 and year_album < 2024)
);

CREATE TABLE IF NOT EXISTS Artist_album (
id_artist INTEGER REFERENCES Artist_list (id_artist),
id_album INTEGER REFERENCES Album_list (id_album),
constraint pk_Artist_album PRIMARY KEY (id_artist, id_album)
);

CREATE TABLE IF NOT EXISTS Track_list (
id_track SERIAL PRIMARY KEY,
id_album INTEGER NOT NULL REFERENCES Album_list (id_album),
name_track VARCHAR(120) NOT NULL,
length_track INTEGER NOT null constraint length_track check (length_track > 0), -- в секундах
constraint pk_Track_list UNIQUE (name_track, id_album)
);

CREATE TABLE IF NOT EXISTS Collection_list (
id_collection SERIAL PRIMARY KEY,
name_collection VARCHAR(60) NOT NULL,
year_collection INTEGER CHECK (year_collection > 2000 and year_collection < 2024)
);

CREATE TABLE IF NOT EXISTS Collection_track (
id_collection INTEGER REFERENCES Collection_list (id_collection),
id_track INTEGER REFERENCES Track_list (id_track),
constraint pk_Collection_track PRIMARY KEY (id_collection, id_track)
);