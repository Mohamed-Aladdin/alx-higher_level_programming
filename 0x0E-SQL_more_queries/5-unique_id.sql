-- list all dbs
-- query dbs

CREATE TABLE IF NOT EXISTS unique_id (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
) ENGINE=INNODB;
