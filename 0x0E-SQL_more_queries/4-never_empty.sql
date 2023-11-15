--  a script that creates the table id_not_null on your MySQL server

CREATE TABLE IF NOT EXITSTS id_not_null(
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);