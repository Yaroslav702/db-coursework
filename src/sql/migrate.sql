CREATE TABLE Permission (
    id INT SERIAL PRIMARY KEY,
    name_of_permission VARCHAR(45) NOT NULL,
    description_of_permission TEXT NOT NULL,
    role_permission INT NOT NULL,
    FOREIGN KEY (role_permission) REFERENCES Role(id) ON DELETE CASCADE
);

CREATE TABLE Role (
    id INT SERIAL PRIMARY KEY,
    role_name VARCHAR(45) NOT NULL, 
    user_role INT,
    role_description TEXT NOT NULL,
    FOREIGN KEY (user_role) REFERENCES User(id) ON DELETE SET NULL
);

CREATE TABLE User (
    id INT SERIAL PRIMARY KEY,
    user_name VARCHAR(45) NOT NULL, 
    user_lastname VARCHAR(45) NOT NULL,
    user_password VARCHAR(255) NOT NULL
);

CREATE TABLE Survey (
    id INT SERIAL PRIMARY KEY,
    survey_name VARCHAR(45) NOT NULL,
    survey_description TEXT NOT NULL,
    survey_result INT NULL,
    survey_user INT NOT NULL,
    FOREIGN KEY (survey_result) REFERENCES Result(id) ON DELETE SET NULL,
    FOREIGN KEY (survey_user) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE Result (
    id INT SERIAL PRIMARY KEY,
    result_name VARCHAR(45) NOT NULL,
    result_description TEXT NOT NULL
);
