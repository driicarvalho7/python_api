use database postgres;

create schema api_py;

create table api_py.user (
	id SERIAL not null,
	name varchar(100),
	email varchar(200),
	password varchar(15)
);

create table api_py.item (
	id SERIAL not null,
	name varchar(100),
	description varchar(200)
);

SELECT * FROM api_py.user ;