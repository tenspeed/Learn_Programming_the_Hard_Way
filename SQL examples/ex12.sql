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
ALTER TABLE peoples ADD COLUMN hadtred INTEGER;

/* rename peoples back to person */
ALTER TABLE peoples RENAME TO person;

.schema person

/* we don't need that */
DROP TABLE person;