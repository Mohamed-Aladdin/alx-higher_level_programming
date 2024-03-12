-- list all dbs
-- query dbs

SELECT state, MAX(value) AS "max_temp" FROM temperatures GROUP BY state ORDER BY state ASC;
