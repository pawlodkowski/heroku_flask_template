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
heroku create <my-app-name>
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


## Further Resources

- [Official python heroku tutorial](https://devcenter.heroku.com/articles/getting-started-with-python) using Django
