-- creates the table unique_id
-- description: id INT with the default value 1 and must be unique
-- name VARCHAR(256)
-- The database name will be an argument of the command
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
