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
    start_time INT,
    duration INT,
    description VARCHAR(255)
);

CREATE TABLE bookings(
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id),
    gymclass_id INT REFERENCES gymclasses(id)
);