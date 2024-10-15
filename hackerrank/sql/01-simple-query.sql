select * from city where population > 100000 and countrycode = 'USA';
select name from city where population > 120000 and countrycode = 'USA';
select * from city;
select * from city where id=1661;
select * from city where countrycode='JPN';
select name from city where countrycode='JPN';

select city, state from station;
select distinct city from station where mod(id, 2) = 0;

select distinct (select count(city) from station) - 
                (select count(distinct city) from station) 
    from station;

select * from 
    (select city, length(city) from station where length(city) <= 
        all (select length(city) from station) order by city limit 1) as d
    union all 
    (select city, length(city) from station where length(city) >= 
        all (select length(city) from station) order by city limit 1);