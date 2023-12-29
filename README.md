# PoleStarLogisitics

Inside PoleStarLogisitics there is a Django web application(ShipAnalysis) that provides a REST API for tracking ships and their positions. It includes a Leaflet.js map interface for visualizing ship locations.

## Features

- List all ships available in the database. (localhost:8000//api/ships/)
- Retrieve and display positions of ships in descending order of timestamp. (localhost:8000/api/positions/<imo>/)
- Visualize ship positions on a map with an interactive front end. (localhost:8000/)

## Requirements

- Python 3.7+
- Django 3.2+
- Django REST Framework
- PostgreSQL with PostGIS extension
- Leaflet.js for front-end map visualization

## Running in Docker

1. **Build and Run with Docker Compose:** Use Docker Compose to build and run the containers for the Django app and the database:
     `docker-compose up --build`
2. **Import CSV Data**: The file which is provided in the assignment is already copied in the project directory only, populate data:
    `docker-compose exec web python manage.py import_csv ship_analysis/management/data/positions.csv`
	- NOTE: this scripts assume there only three ships as provided in the assignments, **you should run it only once, as it will create duplicate entries for positions.**
3. **Create a Superuser (Optional):** If you need access to the Django admin interface, create a superuser account:
    `docker-compose exec web python manage.py createsuperuser`
Now, the application should be accessible at the URLs provided in the Features section above.

## Usage

After installation, you can access the following endpoints:

- `http://localhost:8000/api/ships/` to list all ships.
- `http://localhost:8000/api/positions/<imo>/` to retrieve positions for a specific ship by IMO number.
- `http://localhost:8000/` to view the interactive map with ship positions.

## Stopping the Application

To stop the application and remove the containers, you can use:
`docker-compose down`
## Cleaning Up

To remove everything, including Docker images, you can run:

`docker-compose down --rmi all`
`docker-compose down -v`


## Tasks Explanation

- Design a relational database schema to store the data for the Ships and their Positions.
	- refer `ship_analysis.models`.
- Write Python code to automatically load the CSV data into a relational database
	- refer `ship_analysis/management/commands/import_csv.py`
- Write, using Python, a REST API that implements 2 endpoints:
	- refer
		- `http://localhost:8000/api/ships/`
		- `http://localhost:8000/api/positions/9632179/`
- Graphical Representation
	- `http://localhost:8000/`
- Docker File
	- Above solution uses docker
