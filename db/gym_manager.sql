DROP TABLE bookings;
DROP TABLE members;
DROP TABLE gymclasses;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    membership_type VARCHAR(255)
);

CREATE TABLE gymclasses(
    id SERIAL PRIMARY KEY,
    activity_name VARCHAR(255),
    start_time VARCHAR(255),
    duration INT,
    description VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    gymclass_id INT REFERENCES gymclasses(id) ON DELETE CASCADE
);