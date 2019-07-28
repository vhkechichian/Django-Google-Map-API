# django-google-maps
Basic example of how to use Google Maps with Django and PostGIS 

![](https://raw.githubusercontent.com/LegolasVzla/django-google-maps/master/core/frontend/static/media/app_image.jpeg "App Image")

## Technologies
- [Django REST framework](https://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

- [PostgreSQL](https://www.postgresql.org/) is the World's Most Advanced Open Source Relational Database.

- [PostGIS](http://postgis.net/) is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL.

## Requirements
- Ubuntu 18
- Install PostgreSQL:
```
  sudo apt-get update
  sudo apt install python3-dev postgresql postgresql-contrib python3-psycopg2 libpq-dev
```
- Install PostGIS
```
  sudo apt-get install postgis
```

## Installation

Clone this project:

	git clone https://github.com/LegolasVzla/django-google-maps.git

Create your virtualenv and install the requirements:

	virtualenv env --python=python3
	source env/bin/activate

	pip install -r requirements.txt

In "django-google-maps/core/" path, create logs folder:

	mkdir logs

Create a **settings.ini** file, with the structure as below:

	[postgresdbConf]
	DB_ENGINE=django.contrib.gis.db.backends.postgis
	DB_NAME=dbname
	DB_USER=user
	DB_PASS=password
	DB_HOST=host
	DB_PORT=port

	[GEOSGeometryConf]
	max_distance=5

	[googleMapsConf]
 	API_KEY=yourGoogleAPIKey
	defaultLat=<Your_default_latitude>
 	defaultLng=<Your_default_lingitude>

By default, DB_HOST and DB_PORT in PostgreSQL are localhost/5432. A 'max_distance' suggested could be from 1-5 kilometers, to display nearby places. Also, if you have a Font Awesome key for icons, you can add it in the **settings.ini** file:

	[font-awesomeConf]
	KEY=your_key

Then, run the migrations:

	python manage.py makemigrations

	python manage.py migrate

And finally, run the server:

	python manage.py runserver

You could see the home page in:

	http://127.0.0.1:8000/index/

The map will be setting in the 'defaultLat' and 'defaultLng' position.

## Models

- Spots: table to store places of the users. This table contains a position (PostGIS geometry) column that works to store information of latitude and longitude in WGS 84 format.

## Endpoints Structure for Spots API
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods (GET, POST, PUT, DELETE), making all posssible CRUD (create, retrieve, update, delete) operations.
	
	http://127.0.0.1:8000/api/spots/

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`api/<instance>` | GET | READ | Get all the <instance> record
`api/<instance>/:id` | GET | READ | Get a single <instance> reacord
`api/<instance>`| POST | CREATE | Create a new <instance> record
`api/<instance>/:id` | PUT | UPDATE | Update a <instance> record
`api/<instance>/:id` | DELETE | DELETE | Delete a <instance> record

## Actions

- CRUD:

1. Add a custom place (CREATE): in "GoogleMaps" tab, you can create a new spot doing click in a position of the map and then doing click in "Add a Place" buttom, fill up the form and save your spot.

2. See spots details (READ): in "My Spot List" tab, you can see all the details of your spot list. 

3. Edit spots (UPDATE): in "My Spot List" tab, you can edit spots.

4. Remove a place (DELETE): in "My Spot List" tab, you can delete an spot in the garbage icon.

- Nearby places: in "GoogleMaps" tab, you can display nearby places from your current position within 'max_distance'. The map will show your nearby places with the icon below:
![](https://raw.githubusercontent.com/LegolasVzla/django-google-maps/master/core/frontend/static/media/place_icon.png "Custom Spot")

## Contributions
------------------------

I started this project from [yt-google-maps-1](https://github.com/Klerith/yt-google-maps-1) repository.

All work to improve performance is good

Enjoy it!
