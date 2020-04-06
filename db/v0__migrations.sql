CREATE TABLE migrations(
    id      SERIAL PRIMARY KEY
  , ts      TIMESTAMP
  , name    TEXT
  , comment TEXT
);