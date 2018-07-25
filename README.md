[![Build Status](https://travis-ci.com/kpi-web-guild/django-girls-blog-serhii73.svg?branch=master)](https://travis-ci.com/kpi-web-guild/django-girls-blog-serhii73)
# django-girls-blog-serhii73
##### This is a simple blog based on the djangogirl's tutorial.

### Installation
- [Locally](#locally)
- [Heroku](#heroku)

##### Locally:
1. Clone this repository
2. Install [Python 3.7.0](https://www.python.org/downloads/)
3. [Create and to activate the virtual environment](https://docs.python.org/3.6/library/venv.html)
4. Install requirements for the project: `pip install -r requirements.txt`
5. Add .env in folder, like in .env.example.
6. Create tables for models in your database: `python manage.py migrate`
7. Create superuser for admin page: `python manage.py createsuperuser`
8. Run server: `python manage.py runserver`


##### Heroku:
1. Clone this repository
2. Register account on [Heroku](https://www.heroku.com/)
3.  Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) locally
4. Login to Heroku: `heroku login`
5. Create name of your site: `heroku create <name-of-site>`
6. Deploy to Heroku!: `git push heroku master`
7. Start web process: `heroku ps:scale web=1`
8. Run the migrate and createsuperuser commands: `heroku run python manage.py migrate` and then `heroku run python manage.py createsuperuser`
9. Visit your application: `heroku open`
