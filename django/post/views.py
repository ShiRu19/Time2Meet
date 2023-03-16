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

class AboutUs(ListView):
    model = Project
    template_name = 'post_aboutUs.html'

def createProject(request):
    projectName = request.POST.get('projectName')
    availableTime = ""
    for i in range(70):
        availableTime += ",0"
    availableTime = availableTime[1:]
    if projectName is not None:
        cuser = Project.objects.create(projectName=projectName, availableTime=availableTime)
        cuser.save()
        return redirect("PostFillOutForm", pk=cuser.pk)

def createUser(request):
    userName = request.GET.get('userName')
    userPassword = request.GET.get('userPassword')
    projectId = request.GET.get('projectId')

    result_verifySignUpData = UserSignUp.verifyUserSignUpData(projectId, userName)
    if not result_verifySignUpData:
        result_createUser = dict()
        result_createUser["result"] = "User already exists"
        return HttpResponse(json.dumps(result_createUser))
    else:
        result_createUser = UserSignUp.createUser(userName, userPassword, projectId)
        if result_createUser["result"]:
            result_createUser["result"] = "Sign up success"
        else:
            result_createUser["result"] = "Sign up error"
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

def updateAvailableTime_user(request):
    projectId = request.GET.get('projectId')
    userId = request.GET.get('userId')
    availableTime = request.GET.get('availableTime')
    result_updateUserAvailableTime = AvailableTime.updateAvailableTime_user(projectId, userId, availableTime)
    if(result_updateUserAvailableTime):
        return HttpResponse("Update success")

def updateAvailableTime_project(request):
    projectId = request.GET.get('projectId')
    availableTime = request.GET.get('availableTime')
    result_updateAvailableTime_project = AvailableTime.updateAvailableTime_project(projectId, availableTime)
    if(result_updateAvailableTime_project):
        return HttpResponse("Update success")

def getAllAvailableTime_user(request):
    userId = request.GET.get('userId')
    result_getAllAvailableTime_user = AvailableTime.getAllAvailableTime_user(userId)
    return HttpResponse(json.dumps(result_getAllAvailableTime_user))

def getAvailableTime_allUser(request):
    projectId = request.GET.get('projectId')
    result_getAvailableTime_allUser = AvailableTime.getAvailableTime_allUser(projectId)
    return HttpResponse(json.dumps(result_getAvailableTime_allUser))

def getAllAvailableTime_project(request):
    projectId = request.GET.get('projectId')
    result_getAllAvailableTime_project = AvailableTime.getAllAvailableTime_project(projectId)
    return HttpResponse(json.dumps(result_getAllAvailableTime_project))

def getUserCount(request):
    projectId = request.GET.get('projectId')
    result_getUserCount = Participation.objects.filter(projectId=projectId)
    return HttpResponse(result_getUserCount.count())
