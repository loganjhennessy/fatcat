PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS company (
    id          TEXT PRIMARY KEY
  , symbol      TEXT
  , name        TEXT
  , description TEXT
  , industry    TEXT
  , sector      TEXT
  , exchange    TEXT
  , website     TEXT
  , ceo         TEXT
);

CREATE TABLE IF NOT EXISTS metric (
    id            TEXT PRIMARY KEY
  , abbreviation  TEXT
  , name          TEXT
  , description   TEXT
);

CREATE TABLE IF NOT EXISTS statement (
    statement_id  TEXT NOT NULL PRIMARY KEY
  , metric_id     TEXT
  , company_id    TEXT REFERENCES company  (id)
  , value         NUMERIC(50, 12)
  , date          DATE
  , FOREIGN KEY(metric_id) REFERENCES metric(id)
  , FOREIGN KEY(company_id) REFERENCES company(id)
);