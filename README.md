  ## Learn Django by creating a polls app. [Django documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)


## Creating a project

- To create a project in Django run the following command

`django-admin startproject nameOfTheProject`

- This will create a `nameOfTheProject` directory in your current directory

## Development Server

- To check if everything is installed, run the following command

` python manage.py runserver `

## Creating the polls app

 - Django comes with a utility that automatically generates the basic directory structure of an app, so you can focus on writing code rather than creating directories.

 ## Projects vs. apps

 - What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.
 ## Creating Models

 - A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing
- In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.[polls app](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/models.py)

### Activating models

That small bit of model code gives Django a lot of information. With it, Django is able to:

- Create a database schema (CREATE TABLE statements) for this app.
- Create a Python database-access API for accessing Question and Choice objects.

But first we need to tell our project that the polls app is installed. 

- To include the app in our project, we need to add a reference to its configuration class in the INSTALLED_APPS setting, that's [polls.py](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/apps.py) to [settings.py(installed app section)](https://github.com/kihuni/Learn-Django/blob/main/test_site/test_site/settings.py)

### Three-step guide to keep in mind when making changes to your models:

- Change your models (in models.py).
- Run `python manage.py makemigrations` to create migrations for those changes
- Run `python manage.py migrate` to apply those changes to the database

### __str__()

##### Model.__str__()

The `__str__()` method is called whenever you call str() on an object. Django uses str(obj) in a number of places. Most notably, to display an object in the Django admin site and as the value inserted into a template when it displays an object. Thus, you should always return a nice, human-readable representation of the model from the `__str__()` method.

For example:

```

from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

```
[Adding __str__()](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/models.py)
