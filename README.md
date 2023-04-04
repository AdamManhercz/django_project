# Meal planner Django project

## Description
To create an application that is designed to help in organizing one's meals for the upcoming week. Besides the functional standpoint, the exercise provided me a good opportunity to work with a specific framework and to gain a small insight into complex Python coding.

## Table of contents
1. [Applied tools](#applied-tools)
2. [How to run the application?](#how-to-run-the-application)
3. [Functional description](#functional-description)
4. [Repository content](#repository-content)
5. [Notable](#notable)

## Applied tools

1. Languages:
- [Python](https://www.python.org/)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

2. Libraries
- [Django](https://www.djangoproject.com/)
- [Django REST framework](https://www.django-rest-framework.org/)
- [dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [coverage](https://coverage.readthedocs.io/en/7.2.2/)
- [typing](https://docs.python.org/3/library/typing.html)
- [requests](https://requests.readthedocs.io/en/latest/) and [beautifulsoup](https://pypi.org/project/beautifulsoup4/)

3. Tools
- [Docker](https://www.docker.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Docker compose](https://docs.docker.com/compose/)
- [GitHub](https://github.com/) 
- [GitHub Actions](https://docs.github.com/en/actions)
- [Visual Studio Code](https://code.visualstudio.com/)

## How to run the application?

There are two ways of running this application: locally or in a docker container.

Here are the steps:

1. Create a virual environment on your computer: `python -m venv <your venv name>`
2. Activate your venv: `..yourvenv\Scripts\activate`
3. Clone the Github repo on your venv: `git clone https://github.com/AdamManhercz/django_project.git`

### Run on Docker

4. In case, you don't have: download Docker Desktop on your computer, create an account,open it, log in
5. Run docker-compose command in main folder: `docker-compose build`
6. Run the app in your container: `docker-compose up`
7. Open a browser and go http://127.0.0.1:8000

### Run locally

4. Install the dependencies: `pip install -r requirements.txt`
5. Run the app: `python manage.py runserver`
6. Open a browser and go http://127.0.0.1:8000


## Functional description

After opening the app, you need to register by providing your username, password, and email address for authentication to create an account. Once you have an account, you are free to check the app's recipes and add new ones to the database. After getting familiar with the app and recipes, you can request a meal plan for the next week by clicking the "Get a meal plan!" button on the "/recipes" subpage. By clicking the button, you will automatically receive a meal plan with random lunch recommendations from Monday to Friday sent to your submitted email address. When you're done using the application, you can log out.

Since the application is designed with a REST API, you can use the "api/recipe_list" and "api/recipe_list/'recipename'" URLs to GET, POST, and DELETE recipes from the database.

## Repository content

The repository contains the project folder **src**, which has the basic configurations of the django project, including the main setup for the urls. The created main Django application folder **food_planner** contains the essential configurations and customizations of the application, such as the **views.py**, **models.py**, **forms.py**, as well as the **rest_views.py** and **serializers.py** files that are enable the REST API design. 
The **management** folder contains the scraping scripts, which fill up the database of the project, the **templates** folder has the HTML and CSS files for the subpages. The **users** folder contains the backend for the registration, login and logout process.
Each Django application's **tests folder** contains the unit tests. Using **GitHub Actions**, the **'django-test.yml'** file located in the **'.github/workflows'** folder automates the testing of the application with every push and pull request.
Furthermore, **the Dockerfile** and **docker_compose.yml** are configuring the connection between the project and Docker to create an image, then a container, that ensures to run the application in an independent operating system.
I used SQLite, the default Django database, as a database for the app. 
Eventually, **requirements.txt** contains all the dependencies that the application needs to be run and used 


 ## Notable 

 Throughout my project changed, ideas came and went, thus I met lot of supportive and interesting tools within the framework and others that I can connect or use to my application. During my journey I discovered the essentials of the Django framework, learned how to handle **static and media files**, how to have the basics to form the design through **HTML and CSS**, set up the **e-mail backend** of the application, how to create **REST API design**, test my units, connect my application with **Docker**, also get hint from *CI* through **GitHub Actions**. Furthermore, I tried **Celery** and **Advenced Python Scheduler** for periodic tasks.
