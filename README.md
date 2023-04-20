  ## Learn Django by creating a polls app [django documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)


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
 
 ## Creating views
 - To create views, write your views on [polls/views](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/views.py). To call the view, we need to map it to a URL - and for this we need a URLconf.

 - To create a URLconf in the polls directory, create a file called [urls.py](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/urls.py) and map your views to the coresponding URL
 - Finally, we map/point the root url from the project module to point to apps urls.In the [root url](https://github.com/kihuni/Learn-Django/blob/main/test_site/test_site/urls.py) add an import for django.urls.include and insert an include() in the urlpatterns
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
[Adding __str__() method](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/models.py)

### Creating an admin user

- To create an admin user, run:

`python3 manage.py createsuperuser`

- Enter your desired username and press enter

`Username: admin`

- You will then be prompted for your desired email address

`Email address: admin@example.com`

- The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```
Password: **********
Password (again): *********
Superuser created successfully.

```
- Start the server and head to the admin route. You will be prompted to enter your username and password

- After successfully logged, You should see a few types of editable content: groups and users. They are provided by django.contrib.auth, the authentication framework shipped by Django.

### Make the poll app modifiable in the admin

- To achieve this, we need to tell the admin that Question objects have an admin interface. To do this, open the polls/admin.py file, and edit it to look like this [polls/admin.py](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/admin.py)

### What is a view

- A view is a type of web page in your django application that generally serves a specific function and has a specific template. For example, in our poll aplication, we'll have the following four views
  
    - Question "index"page :- displays the latest few questions
    - Question "index"page :- displys a question text, with no result but with a form to vote
    - Question "result"page :- display result for a particular question
    - Vote action :- handles  voting for a particular choice in a particular question


 - When for example a user request a page from your website. Django will load [test_site.urls](https://github.com/kihuni/Learn-Django/blob/main/test_site/test_site/urls.py) Python module because it’s pointed to by the ROOT_URLCONF setting. It finds the variable named urlpatterns and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text to the ‘polls.urls’ URLconf for further processing

