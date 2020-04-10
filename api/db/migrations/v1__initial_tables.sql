PRAGMA foreign_keys = ON;

CREATE TABLE company (
    id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
  , symbol      TEXT
  , name        TEXT
  , description TEXT
  , industry    TEXT
  , sector      TEXT
  , exchange    TEXT
  , website     TEXT
  , ceo         TEXT
);

CREATE TABLE metric (
    id            INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
  , abbreviation  TEXT
  , name          TEXT
  , description   TEXT
);

CREATE TABLE statement (
    statement_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
  , metric_id     INTEGER
  , company_id    INTEGER REFERENCES company  (id)
  , value         NUMERIC(50, 12)
  , date          DATE
  , FOREIGN KEY(metric_id) REFERENCES metric(id)
  , FOREIGN KEY(company_id) REFERENCES company(id)
);