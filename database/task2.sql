CREATE TABLE IF NOT EXISTS Genre_list (
id_genre SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Artist_list (
id_artist SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS Genre_artist(
id_genre INTEGER REFERENCES Genre_list (id_genre),
id_artist INTEGER REFERENCES Artist_list (id_artist),
constraint pk_Genre_artist PRIMARY KEY (id_genre, id_artist)
);

CREATE TABLE IF NOT EXISTS Album_list (
id_album SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL UNIQUE,
Year INTEGER CHECK (Year > 2000 and Year < 2024)
);

CREATE TABLE IF NOT EXISTS Artist_album (
id_artist INTEGER REFERENCES Artist_list (id_artist),
id_album INTEGER REFERENCES Album_list (id_album),
constraint pk_Artist_album PRIMARY KEY (id_artist, id_album)
);

CREATE TABLE IF NOT EXISTS Track_list (
id_track SERIAL PRIMARY KEY,
id_album INTEGER NOT NULL REFERENCES Album_list (id_album),
name VARCHAR(120) NOT NULL,
length INTEGER NOT null constraint length check (length > 0), -- в секундах
constraint pk_Track_list UNIQUE (name, id_album)
);

CREATE TABLE IF NOT EXISTS Collection_list (
id_collection SERIAL PRIMARY KEY,
name VARCHAR(60) NOT NULL,
YEAR INTEGER CHECK (year > 2000 and year < 2024)
);

CREATE TABLE IF NOT EXISTS Collection_track (
id_collection INTEGER REFERENCES Collection_list (id_collection),
id_track INTEGER REFERENCES Track_list (id_track),
constraint pk_Collection_track PRIMARY KEY (id_collection, id_track)
);

insert into Genre_list(id_genre, name)
VALUES(1, 'Pock');
insert into Genre_list(id_genre, name)
VALUES(2, 'Soul');
insert into Genre_list(id_genre, name)
VALUES(3, 'Blues');
insert into Genre_list(id_genre, name)
VALUES(4, 'Celtic');
insert into Genre_list(id_genre, name)
VALUES(5, 'Ska-punk');

insert into Artist_list(id_artist, name)
VALUES(1, 'Шевчук');
insert into Artist_list(id_artist, name)
VALUES(2, 'Jon Bon Jovi');
insert into Artist_list(id_artist, name)
VALUES(3, 'Amy Winehouse');
insert into Artist_list(id_artist, name)
VALUES(4, 'Stevie Wonder');
insert into Artist_list(id_artist, name)
VALUES(5, 'Eric Clapton');
insert into Artist_list(id_artist, name)
VALUES(6, 'Чиграков');
insert into Artist_list(id_artist, name)
VALUES(7, 'Loreena McKennitt');
insert into Artist_list(id_artist, name)
VALUES(8, 'Шнуров');


insert into Genre_artist
VALUES(1, 1);
insert into Genre_artist
VALUES(1, 2);
insert into Genre_artist
VALUES(2, 3);
insert into Genre_artist
VALUES(2, 4);
insert into Genre_artist
VALUES(3, 5);
insert into Genre_artist
VALUES(3, 6);
insert into Genre_artist
VALUES(4, 7);
insert into Genre_artist
VALUES(5, 8);

insert into Album_list(id_album, name, Year)
VALUES(1, 'Единочество', 2003);
insert into Album_list(id_album, name, Year)
VALUES(2, 'Творчество в пустоте 2', 2022);
insert into Album_list(id_album, name, Year)
VALUES(3, 'Have a nice day', 2005);
insert into Album_list(id_album, name, Year)
VALUES(4, 'What about now', 2013);
insert into Album_list(id_album, name, Year)
VALUES(5, 'Rehab', 2015);
insert into Album_list(id_album, name, Year)
VALUES(6, 'At The BBC', 2021);
insert into Album_list(id_album, name, Year)
VALUES(7, 'Your Life Your Call', 2016);
insert into Album_list(id_album, name, Year)
VALUES(8, 'Little Water Boy', 2020);
insert into Album_list(id_album, name, Year)
VALUES(9, 'Carl Perkins & Friends', 2006);
insert into Album_list(id_album, name, Year)
VALUES(10, 'Blues Breakers', 2016);
insert into Album_list(id_album, name, Year)
VALUES(11, 'На грани изумруда', 2007);
insert into Album_list(id_album, name, Year)
VALUES(12, 'Волопас', 2016);
insert into Album_list(id_album, name, Year)
VALUES(13, 'A Midwinter Night', 2008);
insert into Album_list(id_album, name, Year)
VALUES(14, 'Lost Souls', 2018);
insert into Album_list(id_album, name, Year)
VALUES(15, 'Точка', 2002);
insert into Album_list(id_album, name, Year)
VALUES(16, 'Всякое', 2018);

insert into Artist_album
VALUES(1, 1);
insert into Artist_album
VALUES(1, 2);
insert into Artist_album
VALUES(2, 3);
insert into Artist_album
VALUES(2, 4);
insert into Artist_album
VALUES(3, 5);
insert into Artist_album
VALUES(3, 6);
insert into Artist_album
VALUES(4, 7);
insert into Artist_album
VALUES(4, 8);
insert into Artist_album
VALUES(5, 9);
insert into Artist_album
VALUES(5, 10);
insert into Artist_album
VALUES(6, 11);
insert into Artist_album
VALUES(6, 12);
insert into Artist_album
VALUES(7, 13);
insert into Artist_album
VALUES(7, 14);
insert into Artist_album
VALUES(8, 15);
insert into Artist_album
VALUES(8, 16);


insert into Track_list(id_track, id_album, name, length)
VALUES(1, 1, 'Когда един', 206);
insert into Track_list(id_track, id_album, name, length)
VALUES(2, 1, 'Рождество', 148);
insert into Track_list(id_track, id_album, name, length)
VALUES(3, 2, 'В Раю одиноко', 248);
insert into Track_list(id_track, id_album, name, length)
VALUES(4, 2, 'Время твоей любви', 208);
insert into Track_list(id_track, id_album, name, length)
VALUES(5, 3, 'I am', 233);
insert into Track_list(id_track, id_album, name, length)
VALUES(6, 3, 'Bells of Freedom', 295);
insert into Track_list(id_track, id_album, name, length)
VALUES(7, 4, 'Army of One', 275);
insert into Track_list(id_track, id_album, name, length)
VALUES(8, 4, 'Pictures of You', 238);
insert into Track_list(id_track, id_album, name, length)
VALUES(9, 5, 'Vodafone Live At TBA', 220);
insert into Track_list(id_track, id_album, name, length)
VALUES(10, 5, 'Pharoahe Monch Remix', 216);
insert into Track_list(id_track, id_album, name, length)
VALUES(11, 6, 'Live From The Mercury Prize Awards', 230);
insert into Track_list(id_track, id_album, name, length)
VALUES(12, 6, 'Live On Jools Holland Hootenanny', 276);
insert into Track_list(id_track, id_album, name, length)
VALUES(13, 7, 'My Baby_s Gone', 150);
insert into Track_list(id_track, id_album, name, length)
VALUES(14, 7, 'Mary Ann', 179);
insert into Track_list(id_track, id_album, name, length)
VALUES(15, 8, 'Wondering', 172);
insert into Track_list(id_track, id_album, name, length)
VALUES(16, 8, 'Little Water Boy', 156);
insert into Track_list(id_track, id_album, name, length)
VALUES(17, 9, 'Honey Don_t', 246);
insert into Track_list(id_track, id_album, name, length)
VALUES(18, 9, 'What Kind of Girl ', 166);
insert into Track_list(id_track, id_album, name, length)
VALUES(19, 10, 'Little Girl', 156);
insert into Track_list(id_track, id_album, name, length)
VALUES(20, 10, 'Have You Heard', 358);
insert into Track_list(id_track, id_album, name, length)
VALUES(21, 11, 'Бронзовая птица ', 228);
insert into Track_list(id_track, id_album, name, length)
VALUES(22, 11, 'Мой дорогой, позвони мне рано утром', 224);
insert into Track_list(id_track, id_album, name, length)
VALUES(23, 12, 'Волопас (Левосторонний)', 325);
insert into Track_list(id_track, id_album, name, length)
VALUES(24, 12, 'Волопас (Правосторонний)', 325);
insert into Track_list(id_track, id_album, name, length)
VALUES(25, 13, 'Good King Wenceslas', 198);
insert into Track_list(id_track, id_album, name, length)
VALUES(26, 13, 'Snow', 307);
insert into Track_list(id_track, id_album, name, length)
VALUES(27, 14, 'A Hundred Wishes', 274);
insert into Track_list(id_track, id_album, name, length)
VALUES(28, 14, 'Lost Souls', 309);
insert into Track_list(id_track, id_album, name, length)
VALUES(29, 15, 'Злая пуля', 273);
insert into Track_list(id_track, id_album, name, length)
VALUES(30, 15, 'Однажды', 164);
insert into Track_list(id_track, id_album, name, length)
VALUES(31, 16, 'Эстетика', 163);
insert into Track_list(id_track, id_album, name, length)
VALUES(32, 16, 'Амплуа', 144);

insert into Collection_list(id_collection, name, Year)
VALUES(1, 'Collection DDT', 2023);
insert into Collection_list(id_collection, name, Year)
VALUES(2, 'Collection Bon Jovi', 2022);
insert into Collection_list(id_collection, name, Year)
VALUES(3, 'Collection Amy Winehouse', 2021);
insert into Collection_list(id_collection, name, Year)
VALUES(4, 'Collection Stevie Wonder', 2020);
insert into Collection_list(id_collection, name, Year)
VALUES(5, 'Collection Eric Clapton', 2019);
insert into Collection_list(id_collection, name, Year)
VALUES(6, 'Collection Чиж & Co', 2018);
insert into Collection_list(id_collection, name, Year)
VALUES(7, 'Collection Loreena McKennitt', 2017);
insert into Collection_list(id_collection, name, Year)
VALUES(8, 'Collection Ленинград', 2018);

insert into Collection_track(id_collection, id_track)
VALUES(1, 1);
insert into Collection_track(id_collection, id_track)
VALUES(1, 2);
insert into Collection_track(id_collection, id_track)
VALUES(1, 3);
insert into Collection_track(id_collection, id_track)
VALUES(1, 4);
insert into Collection_track(id_collection, id_track)
VALUES(2, 5);
insert into Collection_track(id_collection, id_track)
VALUES(2, 6);
insert into Collection_track(id_collection, id_track)
VALUES(2, 7);
insert into Collection_track(id_collection, id_track)
VALUES(2, 8);
insert into Collection_track(id_collection, id_track)
VALUES(3, 9);
insert into Collection_track(id_collection, id_track)
VALUES(3, 10);
insert into Collection_track(id_collection, id_track)
VALUES(3, 11);
insert into Collection_track(id_collection, id_track)
VALUES(3, 12);
insert into Collection_track(id_collection, id_track)
VALUES(4, 13);
insert into Collection_track(id_collection, id_track)
VALUES(4, 14);
insert into Collection_track(id_collection, id_track)
VALUES(4, 15);
insert into Collection_track(id_collection, id_track)
VALUES(4, 16);
insert into Collection_track(id_collection, id_track)
VALUES(5, 17);
insert into Collection_track(id_collection, id_track)
VALUES(5, 18);
insert into Collection_track(id_collection, id_track)
VALUES(5, 19);
insert into Collection_track(id_collection, id_track)
VALUES(5, 20);
insert into Collection_track(id_collection, id_track)
VALUES(6, 21);
insert into Collection_track(id_collection, id_track)
VALUES(6, 22);
insert into Collection_track(id_collection, id_track)
VALUES(6, 23);
insert into Collection_track(id_collection, id_track)
VALUES(6, 24);
insert into Collection_track(id_collection, id_track)
VALUES(7, 25);
insert into Collection_track(id_collection, id_track)
VALUES(7, 26);
insert into Collection_track(id_collection, id_track)
VALUES(7, 27);
insert into Collection_track(id_collection, id_track)
VALUES(7, 28);
insert into Collection_track(id_collection, id_track)
VALUES(8, 29);
insert into Collection_track(id_collection, id_track)
VALUES(8, 30);
insert into Collection_track(id_collection, id_track)
VALUES(8, 31);
insert into Collection_track(id_collection, id_track)
VALUES(8, 32);

--название и год выхода альбомов, вышедших в 2018 году
select name, year from album_list
where year = 2018;

--название и продолжительность самого длительного трека
select name, length from track_list
order by length desc
limit 1;

--название треков, продолжительность которых не менее 3,5 минуты
select name, length from track_list
where length > 210;

--названия сборников, вышедших в период с 2018 по 2020 год включительно
select name, year from collection_list
where year >= 2018 and year <= 2020;

--названия сборников, вышедших в период с 2018 по 2020 год включительно
--второй вариант
select name, year from collection_list
where year between 2018 and 2020;

--исполнители, чье имя состоит из 1 слова
select name from artist_list
where name not like '% %';

--название треков, которые содержат слово "мой"/"my"
select name from track_list
where name like 'My %' or name like '% my %';

select name from track_list
where name like 'Мой %' or name like '% мой %';
