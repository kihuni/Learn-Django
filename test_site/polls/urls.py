from django.urls import path

from .import views

# This adds namespace to the application
app_name = "polls"

urlpatterns =[
    path('', views.index, name='index'),

    # the 'name' value as called by the {% url %} template tag
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/result/", views.result, name='result'),
    path("<int:question_id>/vote/", views.vote, name="vote")
]