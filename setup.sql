--Create user table
CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name VARCHAR(45),
    last_name VARCHAR(45),
    hobbies TEXT,
    vehicle VARCHAR(45),
    active BOOLEAN DEFAULT 1
);
-----------------------------------------------------------------------------
--INSERT test records:
-----------------------------------------------------------------------------
INSERT INTO user(
        first_name,
        last_name,
        hobbies,
        vehicle
    )
VALUES (
        "John",
        "Doe",
        "Playing golf",
        "Ford Mustang"
    );
INSERT INTO user(
        first_name,
        last_name,
        hobbies,
        vehicle
    )
VALUES (
        "Mario",
        "Camarillo",
        "microcontrollers",
        "Honda Accord"
    );
INSERT INTO user(
        first_name,
        last_name,
        hobbies,
        vehicle
    )
VALUES (
        "Jay",
        "Douglas",
        "run",
        "Toyota Corolla"
    );