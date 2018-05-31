# ecbscrapper
RSS Euro exchange scrapper

Simple RSS exchange feed reader with Django REST API exporting saved data. Daily exchange rates are imported to database by command.

# Quickstart

1. Generate currencies by:

`python manage.py generate_basic_currencies`

2. To run a scrapper and import exchange rates for given currencies:

`python manage.py run_scrapper`

3. Run server and go to `/api/` URL.
