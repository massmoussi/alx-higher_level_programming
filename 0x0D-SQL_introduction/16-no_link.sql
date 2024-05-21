-- list all rcrds wher name is not Null with a DESC order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
