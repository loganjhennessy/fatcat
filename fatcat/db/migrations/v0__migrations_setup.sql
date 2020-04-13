CREATE TABLE IF NOT EXISTS migrations(
    id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
  , ts      TEXT
  , name    TEXT
  , comment TEXT
);