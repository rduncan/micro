
INSERT INTO authors(first_name,last_name)
    VALUES('Jim', 'Butcher');

INSERT INTO authors(first_name, last_name)
    VALUES('Stephen', 'King');


INSERT INTO books(title, author)
    SELECT 'Skin Game', id
        FROM authors WHERE last_name = 'Butcher';

INSERT INTO books(title, author)
    SELECT 'IT', id
        FROM authors WHERE last_name = 'King';
