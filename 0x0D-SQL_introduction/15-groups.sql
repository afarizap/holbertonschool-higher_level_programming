-- lists the number of records with the same score in the table second_table
-- of the database hbtn_0c_0 in your MySQL server.
ALTER TABLE second_table
ADD COLUMN number int;

UPDATE second_table
SET number = COUNT(score);

SELECT score,
       number
FROM second_table
ORDER BY number;
