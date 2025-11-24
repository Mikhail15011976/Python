--Продвинутая выборка данных


--количество исполнителей в каждом жанре !

select name_genre, count(id_artist) artist_q from Genre_list g
join genre_artist a on g.id_genre = a.id_genre
group by g.name_genre 
order by artist_q desc;
 
--количество треков, вошедших в альбомы 2019-2020 годов !

select tl.name_track, al.year_album from album_list al 
join track_list tl on al.id_album = tl.id_album 
where al.year_album between 2019 and 2020;

--средняя продолжительность треков по каждому альбому !

select al.name_album, avg(tl.length_track) from album_list al 
join track_list tl on al.id_album = tl.id_album 
group by al.name_album 
order by avg(tl.length_track) desc;

--все исполнители, которые не выпустили альбомы в 2020 году !

select al.name_artist from artist_list al 
join artist_album aa on al.id_artist = aa.id_artist 
join album_list al2 on aa.id_album = al2.id_album 
where al2.year_album != 2020
group by al.name_artist;

--названия сборников, в которых присутствует конкретный исполнитель (выберите сами) !

select distinct name_collection from collection_list cl 
join collection_track ct on cl.id_collection = ct.id_collection 
join track_list tl on ct.id_track = tl.id_track 
join album_list al on tl.id_album = al.id_album 
join artist_album aa on al.id_album = aa.id_album 
join artist_list al2 on aa.id_artist = al2.id_artist 
where name_artist = 'Шнуров';

--название альбомов, в которых присутствуют исполнители более 1 жанра !

select distinct al.name_album, count(id_genre) from album_list al 
join artist_album aa on al.id_album = aa.id_album 
join artist_list al2 on aa.id_artist = al2.id_artist 
join genre_artist ga on al2.id_artist = ga.id_artist 
group by al.name_album 
having count(id_genre) > 1;

-- наименование треков, которые не входят в сборники !

select tl.name_track from track_list tl 
left join collection_track ct on tl.id_track = ct.id_track 
where ct.id_track is null;

--исполнителя(-ей), написавшего самый короткий по продолжительности трек (теоретически таких треков может быть несколько)  !

select al.name_artist, tl.length_track from artist_list al 
join artist_album aa on al.id_artist = aa.id_artist 
join album_list al2 on aa.id_album = al2.id_album 
join track_list tl on al2.id_album = tl.id_album 
where tl.length_track = (select min(length_track) from track_list tl2)
order by length_track desc;


--название альбомов, содержащих наименьшее количество треков !

select al.name_album, count(*) from album_list al 
join track_list tl on al.id_album = tl.id_album 
group by al.name_album 
order by count(*)
limit 1;
