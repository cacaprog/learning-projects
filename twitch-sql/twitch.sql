-- Question 1
/*
SELECT * 
FROM chat
LIMIT 10;

SELECT * 
FROM stream
LIMIT 10;

-- question 2
select distinct game
from stream
where game is not null;


-- question 3
select distinct channel
from stream;


-- question 4
select game, count(*) as viewers
from stream
group by 1
order by 2 desc;

-- question 5
select country, count(*)
from stream
where game = 'League of Legends' and country is not null
group by 1
order by 2 desc;

-- question 6
/*
select player
	,count(*)
from stream
group by 1
order by 2 desc
;

-- question 7
select game, 
	case
		when game = 'League of Legends' then 'MOBA'
		when game = 'Dota 2' then 'MOBA'
		when game = 'Heroes of the Storm' then 'MOBA'
		when game = 'Counter-Strike: Global Offensive' then 'FPS'
		when game = 'DayZ' then 'Survival'
		when game = 'ARK: Survival Evolved' then 'Survival'
		else 'Other'
	end as genre
from stream
group by distinct 1
;

-- question 9
-- aqui não aceitou o strftime, adaptei com o código abaixo 
select time, date_part('second', time)
from stream
group by 1
limit 20;


-- question 10
select date_part('hour', time) as hour, count(*) as br_viewers
from stream
where country = 'BR'
group by 1
order by 2 desc;
*/

-- question 11
/*
select * 
from stream s
join chat c
	on s.device_id = c.device_id
;
*/