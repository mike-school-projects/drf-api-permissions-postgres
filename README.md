# LAB - Class 32

## Project: Django Permissions and Postgresql

### Features - General
- You have been supplied with two demos, each presenting a key new feature.
1. One demonstrates how to restrict access to portions of your APIs data. 
2. The other demonstrates switching over to using postgres vs sqlite
- Your job is to merge the functionality of both demos.
- Customize your project to use different application features/models than what was used in demos.

### Features - Django REST Framework
- Make your site a DRF powered API as you did in previous lab.
- Adjust project’s permissions so that only authenticated user’s have access to API.
- Add a custom permission so that only appropriate users can update or delete it.
1. Exactly what this means will depend on your application, so if you have any questions about “appropriate users” means reach out to TA/Instructor.
- Add ability to switch user’s directly from browsable API.

### Features - Docker
- NOTE Refer to demo for built out Dockerfile and docker-compose.yml examples.
- create Dockerfile based off python:3.10-slim
- create docker-compose.yml to run Django app as a web service.
- enter docker compose up --build to start your site.
- add postgres as a service
- Note: It is not required to include a volume so that data can persist when container is shut down.
- Go to browsable api and confirm site properly restricts users based on their permissions.

## Author: Mike Shen

## Links and Resources
N/A 

##  Setup
per requirements.txt

Need to set up .env file in project folder for Django secret key.  See .env.sample

# How to initialize/run your application (where applicable)

From root folder, run:

docker compose up --build

Browse to localhost:8000

## How to use your library (where applicable)

## Tests

From root folder, run:

docker compose run web python manage.py test
