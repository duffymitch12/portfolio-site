PRAGMA foreign_keys = ON;

CREATE TABLE experience (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        company TEXT NOT NULL,
        filename TEXT NOT NULL,
        locationState TEXT NOT NULL,
        locationCity TEXT NOT NULL,
        description TEXT NOT NULL,
        startYear INTEGER,
        endYear INTEGER,
        startMonth TEXT NOT NULL,
        endMonth TEXT NOT NULL
    );