  # Learn Django by creating a polls app. [Full documentation](https://docs.djangoproject.com/en/4.1/intro/tutorial01/)


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

 - What’s the difference between a project and an app? An app is a web application that does something – e.g., a blog system, a database of public records or a small poll app. A project is a collection of configuration and apps for a particular website. A project can contain multiple apps. An app can be in multiple projects.[polls app](https://github.com/kihuni/Learn-Django/blob/main/test_site/polls/models.py)
 
 ## Creating Models

 - A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you’re storing
- In our poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.


