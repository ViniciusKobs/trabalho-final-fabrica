USE market;

INSERT INTO users (
    username,
    password,
    email
)
VALUES (
        'admin',
        'password',
        'email@email.com'
       );

SELECT * FROM users;