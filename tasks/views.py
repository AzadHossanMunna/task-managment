from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("welcome to the task management system")
    
def contact(request):
        return HttpResponse("this is my contact list")
def show_task(request):
      return HttpResponse("this is what it is")
def show_specific_task(request,id):
      print("id",id)
      print("id type",type(id))
      return HttpResponse("This is specific task page")
