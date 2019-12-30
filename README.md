# Twinkle To-Do <br />

Twinkle To-do is an online task manager that helps you keep track of and prioritize tasks.
Each task may have any number of entries, making it easy to add specific steps in order
to complete a particular task. Due dates help keep you on track and efficient.

## Framework & Resources <br />
I'm writing this app using the Django framework, following Eric Matthes's Python Crash
Course as a helpful resource. Below are additional resources you may find helpful:

[freeCodeCamp.org's Python Django Web Framework](https://www.youtube.com/watch?v=F5mRW0jo-U4) <br />
[William Vincent's Django Rest Framework with React Tutorial](https://wsvincent.com/django-rest-framework-react-tutorial/) <br />
[Django Documentation: Deployment Checklist - How not to use SECRET_KEY in production](https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/) <br />

## Instructions to set up the environment<br />
First, create your virtual environment: <br />
- For Mac, I've used the following commands, typed in the terminal:
`$ mkdir Dev` <br />
`$ cd Dev`<br />
`$ virtualenv`<br />
- This should run virtualenv without errors.
`$ virtualenv -p python3 .`<br />
- This runs virtualenv with interpreter /usr/local/bin/python3
- Also installs setuptools, pip, wheel...done.
`$ source bin/activate`<br />
- Use this command to activate your virtualenv each time for Python & Django
`(Dev) $ pip install django==3.0`<br />
`(Dev) $ pip install djangorestframework==3.11.0`<br />
`(Dev) $ pip install django-cors-headers==3.2.0`<br />
- If you are unsure if your virtualenv matches, check with `pip freeze`:
`(Dev) $ pip freeze`<br />

```
asgiref==3.2.3
Django==3.0
django-cors-headers==3.2.0
pytz==2019.3
sqlparse==0.3.0
```
<br />
- In another window, to install `create-react-app` globally:
`$ npm install -g create-react-app`<br />
- Now you can run this app locally.
