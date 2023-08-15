-- script that lists all records of the second_table of the database hbtn_0c_0
-- Don’t list rows without a name value
-- Results should display the score and the name and be listed by descending score
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
