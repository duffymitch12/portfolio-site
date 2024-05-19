PRAGMA foreign_keys = ON;

CREATE TABLE
    experience (
        exp_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(20) NOT NULL,
        company VARCHAR(40) NOT NULL,
        filename VARCHAR(64) NOT NULL,
        locationState VARCHAR(2) NOT NULL,
        locationCity VARCHAR(20) NOT NULL,
        description VARCHAR(256) NOT NULL,
        startYear INTEGER,
        endYear INTEGER,
        startMonth VARCHAR(3) NOT NULL,
        endMonth VARCHAR(10) NOT NULL,
    );