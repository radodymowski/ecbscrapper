# ecbscrapper
RSS Euro exchange scrapper

Simple RSS exchange feed reader with Django REST API exporting saved data. Daily exchange rates are imported to database by command.

# Dependencies

- Python 2.7
- Django 1.11

Used packages are listed in req file.


# Quickstart to run project

1. Create virtualenv and install dependencies by:

`pip install -r req`

2. Generate currencies by:

`python manage.py generate_basic_currencies`

3. To run a scrapper and import exchange rates for given currencies:

`python manage.py run_scrapper`

4. Run server and go to `/api/` URL or import api data from external script, e.g. curl
