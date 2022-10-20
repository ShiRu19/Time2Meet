from contextlib import redirect_stderr, redirect_stdout
from urllib import request, response
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Participation, Project, User
#from django.http import HttpResponse

class PostFillOutForm(DetailView):
    model = Project
    template_name = 'post_userForm.html'

class RegisterProject(ListView):
    model = Project
    template_name = 'post_register.html'

def createProject(request):
    projectName = request.POST.get('projectName')
    if projectName is not None:
        cuser = Project.objects.create(projectName=projectName)
        cuser.save()
        return redirect("PostFillOutForm", pk=cuser.pk)

def createUser(request):
    userName = request.GET.get('userName')
    userPassword = request.GET.get('userPassword')
    if userName is not None:
        cuser = User.objects.create(userName=userName, userPassword=userPassword)
        cuser.save()
        return HttpResponse("Create success")
    return HttpResponse("Create error")
        