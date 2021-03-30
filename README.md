# Getting started with Flask and Heroku

Template for deploying a flask app to heroku. Created for the [Spiced Data Science Bootcamp](https://www.spiced-academy.com/en/program/data-science).

Original template created by [Malte Bonart](https://github.com/bonartm); this version of the template adapted by [Paul Wlodkowski](https://github.com/pawlodkowski).

- Malte's original template can be found here: https://github.com/bonartm/heroku-flask

## Requirements

- free heroku account
- heroku cli installed and set up locally

## Instructions

1. clone the repository

```bash
git clone https://github.com/pawlodkowski/heroku_flask_template.git
cd heroku_flask_template
```

2. create a new heroku app

```bash
heroku create --region eu <my-app-name>
```

3. test the app locally

```bash
heroku local web
```

on windows use

```bash
heroku local web -f Procfile.windows
```

4. push code to heroku

```bash
git push heroku master
```

5. open website in browser

```bash
heroku open
```

6. to delete app

```bash
heroku apps:destroy <my-app-name>
```

## Further Resources

- [Official Python Heroku Tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) using Django
- [Deploying a Dash App](https://dash.plotly.com/deployment) (scroll down to the section on Heroku deployment, which is the free alternative to _Dash Enterprise_).
- [The Flask Mega-Tutorial: Deployment on Heroku](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xviii-deployment-on-heroku)
  - This is overall an excellent, well-written tutorial on all things Flask related. _Miguel Grinberg_ gives you an extensive, step-by-step guide on building an entire social network / blog website from scratch using Flask + all its extensions. You learn a lot of Full Stack Web Development along the way.
