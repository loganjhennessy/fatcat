# Fatcat

Stock screener tool to turn me into a fatcat.

## Setup

### Install dependencies

This app uses poetry for Python dependency version management.

```bash
# Install poetry globally
pip install poetry

# Within a virtualenv
cd fatcat
poetry install
```

The app includes a command-line tool to do setup and basic tasks.

### Create database

To create the sqlite3 database and populate initial tables.

```bash
cd fatcat
python manage.py migrate
```

### Populate database

This requires an API key for Financial Modeling Prep. To obtain one visit [fmpcloud.io](https://fmpcloud.io/). Save that
key to a text file called `fmp_api_key.txt` within the `fatcat` directory (same dir as `manage.py`).

The following call will use that key.

Note, be careful if you only signed up for the trial as this will burn through your limit pretty quick.

```bash
cd fatcat
python manage.py populate-companies
```

## Local serving

```bash
# Backend
cd fatcat
uvicorn app:app

# Frontend
cd app
npm start
```

## Todo

There is still a lot to do. Note that right now the API is not wired up to the database and instead returns one static
object thousands of times.

The frontend is also not completely ready to hook up to the API anyway.

I don't think I want to start with a page listing all companies. I think the next step is to build a page that will
show any one company. When you visit `localhost:3000/DAL`, for instance, it will show the page for DAL. The API call
will go and get the data it needs from FMP if it does not already have it in the sqlite database.

This will progressively fill up the database with companies as I request them, rather than all at once. But if I change
my mind and want to implement a batch job, I can.

Data for this page should include:
* Company profile information (name, description, exchange, etc.)
* Key metrics (BVPS, ROIC, etc)
* "The Big Five" calculated for 10, 5, and 1-year periods
* Sticker price
* Current price

Hypothetically, if I can generate and display this for one company, I can do it for any of them. Although, I'm sure I'll
spend quite a bit of time working around corner-cases and missing data and the like.
