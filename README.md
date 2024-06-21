# Overview

This program retrieves information of a YouTube channel through user input, and its videos using the YouTube Data API, which then stores the information in an SQLite database.

## Project setup & Libraries

- API Key: Obtain a YouTube Data API Key from Google Cloud Console and set it as an environmental variable named 'API_KEY'

```
pip install requests
pip install pandas
pip install --upgrade google-api-python-client
pip install sqlalchemy

```

## Running code & explanation

```
python3 api_project.py

```
1. Suppose you input a channel (with no spaces): "pewdiepie"
- retrieves channel ID using the API
- fetches information on 5 videos from the youtube channel
- stores the information inside the database
- displays the stores data as a Pandas DataFrame
