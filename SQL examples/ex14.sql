ALTER TBLE person ADD COLUMN dead INTEGER;

ALTER TABLE person ADD COLUMN phone_number INTEGER;

ALTER TABLE person ADD COLUMN salary REAL;

ALTER TABLE person ADD COLUMN dob DATETIME;

ALTER TABLE person_pet ADD COLUMN purchased_on DATETIME;

ALTER TABLE pet ADD COLUMN parent INTEGER;

SELECT id FROM person;

UPDATE person SET dead = 0;

UPDATE person SET phone_number = 18009998765
	WHERE person.first_name = "Zed";

UPDATE person SET salary = 80000.00
	WHERE person.first_name = "Zed";

UPDATE person SET dob = 1970
	WHERE person.first_name = "Zed";

UPDATE person_pet SET purchased_on = 1982
	WHERE person_pet.pet_id = 0;

UPDATE person_pet SET purchased_on = 1984
	WHERE person_pet.pet_id = 1;

UPDATE pet SET dob = 1882
	WHERE pet.id = 0;

UPDATE pet SET dob = 1983
	WHERE pet.id = 1;

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (1, "Todd", "Smith", 27, 0, 9999998888, 0.00, 1986);

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (2, "Alven", "Diaz", 25, 0, 1112223333, 100000.00, 1988);

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (3, "Lilia", "Diaz", 24, 0, 2223334444, 40000.00, 1989);

INSERT INTO person (id, first_name, last_name, age, dead, phone_number, salary, dob)
	VALUES (4, "Bryan", "Smith", 31, 0, 5556667777, 40000.00, 1984);

INSERT INTO pet (id, name, breed, age, dead, dob)
	VALUES (2, "Kitty", "Cat", 16, 1, 1993);

INSERT INTO pet (id, name, breed, age, dead, dob)
	VALUES (3, "Luna", "Cat", 3, 0, 2010);

INSERT INTO pet (id, name, breed, age, dead, dob)
	VALUES (4, "Jack", "Dog", 2, 0, 2011);

INSERT INTO pet (id, name, breed, age, dead, dob)
	VALUES (5, "Mowgli", "Bear", 10, 0, 2003);

INSERT INTO pet (id, name, breed, age, dead, dob)
	VALUES (6, "Loki", "Cat", 5, 0, 2008);

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (1, 2, 1993);

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (2, 5, 2003);

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (3, 3, 2013);

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (3, 6, 2013);

INSERT INTO person_pet (person_id, pet_id, purchased_on)
	VALUES (4, 4, 2011);

UPDATE pet SET parent = (SELECT person_id
	FROM person_pet
	WHERE pet.id = person_pet.pet_id
);

SELECT * FROM person;

SELECT * FROM pet;

SELECT * FROM person_pet;

SELECT pet.name, person.first_name FROM pet, person
	WHERE
	pet.id IN (SELECT person_pet.pet_id FROM person_pet
				WHERE person_pet.purchased_on > 2004) AND
	person.id = pet.parent;