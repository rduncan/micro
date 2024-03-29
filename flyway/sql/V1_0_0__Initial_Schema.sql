CREATE TABLE authors (
    id SERIAL NOT NULL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL
);

CREATE TABLE books (
    id SERIAL NOT NULL PRIMARY KEY,
    title VARCHAR(80) NOT NULL,
    author INT NOT NULL REFERENCES authors(id)
);

