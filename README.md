# django_project

## The task
To create an application that is designed to help in organizing one's meals for the upcoming week. Besides the functional standpoint, the exercise provided a good opportunity to work with a specific framework and to gain a small insight into complex Python coding.

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
- [Docker compose](https://docs.docker.com/compose/)
- [GitHub](https://github.com/) 
- [Visual Studio Code](https://code.visualstudio.com/)

## Setup, installation

There are two ways of running this application: locally and in a docker container.

Here are the steps:

1. Create a virual environment on your computer: `python -m venv <your venv name>`
2. Activate your venv: `..yourvenv\Scripts\activate`
3. Clone the Github repo on your venv: `git clone https://github.com/AdamManhercz/django_project.git`


### Run on Docker

4. Download Docker Desktop on your computer, create an account, log in
5. Run docker-compose command in main folder: `docker-compose --build`
6. Run the app in your container: `docker-compose up`
7. Open a browser and go http://127.0.0.1:8000

### Run locally

4. Install the dependencies: `pip install -r requirements.txt`
5. Run the app: `python manage.py runserver`
6. Open a browser and go http://127.0.0.1:8000



## Repo content