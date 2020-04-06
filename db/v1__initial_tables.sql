CREATE TABLE company (
    id          UUID   PRIMARY KEY
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
    id            UUID  PRIMARY KEY
  , abbreviation  TEXT
  , name          TEXT
  , description   TEXT
);

CREATE TABLE statement (
    metric_id     UUID  REFERENCES metric   (id)
  , company_id    UUID  REFERENCES company  (id)
  , value         NUMERIC(50, 12)
  , date          DATE
);