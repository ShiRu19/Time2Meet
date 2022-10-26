from contextlib import redirect_stderr, redirect_stdout
from urllib import request, response
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Participation, Project, User
from static import data
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
    projectId = request.GET.get('projectId')

    result_verifySignUpData = data.verifyUserSignUpData(projectId, userName)
    if not result_verifySignUpData:
            return HttpResponse("User already exists")

    if data.createUser(userName, userPassword, projectId):
        return HttpResponse("Create success")
    else:
        return HttpResponse("Create error")

def userLogin(request):
    userName = request.GET.get('userName')
    userPassword = request.GET.get('userPassword')
    projectId = request.GET.get('projectId')
    result_verifyUserLoginData = data.verifyUserLoginData(projectId, userName, userPassword)
    if(result_verifyUserLoginData):
        return HttpResponse("Login success")
    else:
        return HttpResponse("Wrong user name or password")