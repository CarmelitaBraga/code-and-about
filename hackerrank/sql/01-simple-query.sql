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

select distinct city from station 
where city like 'A%' or 
      city like 'E%' or 
      city like 'I%' or 
      city like 'O%' or 
      city like 'U%';

select distinct city from station 
where city like '%a' or 
      city like '%e' or 
      city like '%i' or 
      city like '%o' or 
      city like '%u';

select distinct city from station 
where upper(left(city, 1)) in ('A', 'E', 'I', 'O', 'U') and 
      upper(right(city, 1)) in ('A', 'E', 'I', 'O', 'U');

select distinct city from station where upper(left(city, 1)) not in ('A', 'E', 'I', 'O', 'U');