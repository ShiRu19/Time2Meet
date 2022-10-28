from contextlib import redirect_stderr, redirect_stdout
import json
from urllib import request, response
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Participation, Project, User
from static.data import UserLogin, UserSignUp, AvailableTime
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

    result_verifySignUpData = UserSignUp.verifyUserSignUpData(projectId, userName)
    if not result_verifySignUpData:
        return HttpResponse("User already exists")

    result_createUser = UserSignUp.createUser(userName, userPassword, projectId)
    if result_createUser["result"]:
        result_createUser["result"] = "Sign up success"
    else:
        result_createUser["result"] = "Sign up error"

    print(result_createUser)
    return HttpResponse(json.dumps(result_createUser))

def userLogin(request):
    userName = request.GET.get('userName')
    userPassword = request.GET.get('userPassword')
    projectId = request.GET.get('projectId')
    result_verifyUserLoginData = UserLogin.verifyUserLoginData(projectId, userName, userPassword)
    if(result_verifyUserLoginData["result"]):
        result_verifyUserLoginData["result"] = "Login success"
    else:
        result_verifyUserLoginData["result"] = "Wrong user name or password"
    
    return HttpResponse(json.dumps(result_verifyUserLoginData))

def updateUserAvailableTime(request):
    projectId = request.GET.get('projectId')
    userId = request.GET.get('userId')
    availableTime = request.GET.get('availableTime')
    print(str(availableTime)+"~~~~~")
    result_updateUserAvailableTime = AvailableTime.updateUserAvailableTime(projectId, userId, availableTime)
    if(result_updateUserAvailableTime):
        return HttpResponse("Update success")

def getAllAvailableTime(request):
    projectId = request.GET.get('projectId')
    result_getAllAvailableTime = AvailableTime.getAllAvailableTime(projectId)
    return HttpResponse(result_getAllAvailableTime)