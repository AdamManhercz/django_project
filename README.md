# Django project

## The task
To create an application that is designed to help in organizing one's meals for the upcoming week. Besides the functional standpoint, the exercise provided me a good opportunity to work with a specific framework and to gain a small insight into complex Python coding.

## Applied tools

1. Languages:
- [Python](https://www.python.org/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

2. Libraries
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [typing](https://docs.python.org/3/library/typing.html)
- [requests](https://requests.readthedocs.io/en/latest/) and [beautifulsoup](https://pypi.org/project/beautifulsoup4/)

3. Tools
- [Docker](https://www.docker.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Docker compose](https://docs.docker.com/compose/)
- [GitHub](https://github.com/) 
- [Visual Studio Code](https://code.visualstudio.com/)

## How to run the application?

There are two ways of running this application: locally or in a docker container.

Here are the steps:

1. Create a virual environment on your computer: `python -m venv <your venv name>`
2. Activate your venv: `..yourvenv\Scripts\activate`
3. Clone the Github repo on your venv: `git clone https://github.com/AdamManhercz/django_project.git`

### Run on Docker

4. In case, you don't have: download Docker Desktop on your computer, create an account,open it, log in
5. Run docker-compose command in main folder: `docker-compose --build`
6. Run the app in your container: `docker-compose up`
7. Open a browser and go http://127.0.0.1:8000

### Run locally

4. Install the dependencies: `pip install -r requirements.txt`
5. Run the app: `python manage.py runserver`
6. Open a browser and go http://127.0.0.1:8000


## Repository content

The repository contains the project folder **src**, which has the basic configurations of the django project, including the main setup for the urls. The created django main application folder **food_planner** contain the essential configurations and customizations of the application, such the **views.py**, **models.py**, **forms.py** as well as the **rest_views.py** and **serializers.py** files that are enable the REST API design. 
The **management** folder contains the scraping scripts that fill up the database of the project, the **templates** folder has the HTML and CSS files for the subpages.The **users** folder contains the backend for the registration, login and logout process.
Furthermore, **the Dockerfile** and **docker_compose.yml** are configuring the connection between the project and Docker to create an image, then a container, that ensures to run the application in an independent operating system. 
I used SQLite, the default Django database, as a database for the app. 
Eventually, **requirements.txt** contains all the dependencies that one needs to run and use the app.
 
