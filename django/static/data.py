from email.policy import HTTP
import json
from post.models import Participation, Project, User, ParticipationDetail
from django.http import HttpResponse
from localStoragePy import localStoragePy

class UserLogin:
    def verifyUserLoginData(projectId, userName, userPassword):
        cparticipation = Participation.objects.filter(projectId=projectId).extra(
            select={'userName': 'user.userName', 'userPassword': 'user.userPassword'},
            tables=['user'],
            where=['participation.userId=user.ID', "user.userName='"+userName+"'", "user.userPassword='"+userPassword+"'"]
        ).values('userId')

        resultDict = {}
        if cparticipation.count() == 0 :
            resultDict["result"] = 0
        else:
            resultDict["result"] = 1
            resultDict["userId"] = cparticipation[0]["userId"]

        return resultDict

class UserSignUp:
    def createUser(userName, userPassword, projectId):
        resultDict = {}
        if userName is not None:
            availableTime = ""
            for i in range(70):
                availableTime += ",0"
            availableTime = availableTime[1:]

            cuser = User.objects.create(userName=userName, userPassword=userPassword, availableTime=availableTime)
            cparticipation = Participation.objects.create(projectId=projectId, userId=cuser.pk)
            resultDict['result'] = 1
            resultDict['userId'] = cuser.pk
            cuser.save()
            cparticipation.save()
        else:
            resultDict['result'] = 0

        return resultDict


    def verifyUserSignUpData(projectId, userName):
        cparticipation = Participation.objects.filter(projectId=projectId).extra(
            select={'userName': 'user.userName', 'userPassword': 'user.userPassword'},
            tables=['user'],
            where=['participation.userId=user.ID', "user.userName='"+userName+"'"]
        )
        if cparticipation.count() == 0 :
            return True
        else:
            return False

class AvailableTime:
    def updateAvailableTime_user(projectId, userId, availableTime):
        cparticipation = Participation.objects.get(userId=userId)
        cparticipation.availableTime = str(availableTime)
        cparticipation.save()
        return True

    def updateAvailableTime_project(projectId, availableTime):
        cproject = Project.objects.get(id=projectId)
        cproject.availableTime = str(availableTime)
        cproject.save()
        return True

    def getAllAvailableTime_user(userId):
        cparticipation = Participation.objects.get(userId=userId)
        userAvailableTime = str(cparticipation.availableTime).split(",")
        return userAvailableTime

    def getAvailableTime_allUser(projectId):
        cparticipation = Participation.objects.filter(projectId=projectId)
        userAvailableTime = {}
        for user_i in cparticipation:
            cuser = User.objects.get(id=user_i.userId)
            userAvailableTime[cuser.userName] = str(user_i.availableTime).split(",")
        return userAvailableTime

    def getAllAvailableTime_project(projectId):
        cproject = Project.objects.get(id=projectId)
        projectAvailableTime = str(cproject.availableTime).split(",")
        return projectAvailableTime