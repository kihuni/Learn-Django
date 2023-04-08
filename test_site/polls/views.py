from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello,world. You are at the polls index.')

def detail(request, question_id):
    return HttpResponse("You're looking at questions %s." % question_id)

def result(request, question_id):
    response = "You're looking at the result of questions %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)