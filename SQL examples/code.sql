DROP TABLE person;

DROP TABLE pet;

DROP TABLE person_pet;

CREATE TABLE person (
	id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	age INTEGER
);

CREATE TABLE pet (
	id INTEGER PRIMARY KEY,
	name TEXT,
	breed TEXT,
	age INTEGER,
	dead INTEGER
);

CREATE TABLE person_pet (
	person_id INTEGER,
	pet_id INTEGER
);

INSERT INTO person (id, first_name, last_name, age)
	VALUES (0, "Zed", "Shaw", 37);

INSERT INTO pet (id, name, breed, age, dead)
	VALUES (0, "Fluffy", "Unicorn", 1000, 0);

INSERT INTO pet VALUES (1, "Gigantor", "Robot", 1, 1);

INSERT INTO person_pet (person_id, pet_id) VALUES (0, 0);
INSERT INTO person_pet VALUES (0, 1);

SELECT * FROM person;

SELECT name, age FROM pet;

SELECT name, age FROM pet WHERE dead = 0;

SELECT * FROM person WHERE first_name != "Zed";

SELECT pet.id, pet.name, pet.age, pet.dead
	FROM pet, person, person_pet
	WHERE
	pet.id = person_pet.pet_id AND
	person_pet.person_id = person.id AND
	person.first_name = "Zed";

/* make sure there's dead pets */
SELECT name, age FROM pet WHERE dead = 1;

/* aww poor robot */
DELETE FROM pet WHERE dead = 1;

/* make sure the robot is gone */
SELECT * FROM pet;

/* let's resurrect the robot */
INSERT INTO pet VALUES (1, "Gigantor", "Robot", 1, 0);

/* the robot LIVES! */
SELECT * FROM pet;

/* this should fail because 0 is already taken. */
INSERT INTO person (id, first_name, last_name, age)
	VALUES (0, "Frank", "Smith", 100);

/* we can force it by doing an INSERT OR REPLACE */
INSERT OR REPLACE INTO person (id, first_name, last_name, age)
	VALUES (0, "Frank", "Smith", 100);

SELECT * FROM person;

/* and shortand for that is just REPLACE */
REPLACE INTO person (id, first_name, last_name, age)
	VALUES (0, "Zed", "Shaw", 37);

/* now you can see I'm back */
SELECT * FROM person;

/* only drop table if it exists */
DROP TABLE IF EXISTS person;

/* create again to work with it */
CREATE TABLE person (
	id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	age INTEGER
);

/* rename the table to peoples */
ALTER TABLE person RENAME TO peoples;

/* add a hatred column to peoples */
ALTER TABLE peoples ADD COLUMN hatred INTEGER;

/* rename peoples back to person */
ALTER TABLE peoples RENAME TO person;

DROP TABLE person;

CREATE TABLE person(
	id INTEGER PRIMARY KEY,
	first_name TEXT,
	last_name TEXT,
	age INTEGER
);

INSERT INTO person (id, first_name, last_name, age)
	VALUES (0, "Zed", "Shaw", 37);

ALTER TABLE pet ADD COLUMN dob DATETIME;

SELECT * FROM person;
SELECT * FROM pet;

.schema person
.schema person_pet
.schema pet

SELECT * FROM person;

SELECT * FROM pet;

SELECT * FROM person_pet;