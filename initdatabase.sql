use whiskeys;

create table whiskey(
    id int NOT NULL AUTO_INCREMENT, 
    name varchar(100), 
    distillery varchar(100), 
    age int, price int, 
    country_id int, 
    PRIMARY KEY(id));