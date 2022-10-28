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
    def updateUserAvailableTime(projectId, userId, availableTime):
        cuser = User.objects.get(id=userId)
        userAvailableTime = str(cuser.availableTime).split(",")
        cproject = Project.objects.get(id=projectId)
        projectAvailableTime = str(cproject.availableTime).split(",")
        newAvailableTime = str(availableTime).split(",")

        newAvailableTime_str = ""
        for i in range(0, len(projectAvailableTime)):
            projectAvailableTime[i] = str(int(projectAvailableTime[i]) - int(userAvailableTime[i]) + int(newAvailableTime[i]))
            newAvailableTime_str += "," + projectAvailableTime[i]
        newAvailableTime_str = newAvailableTime_str[1:]

        cuser.availableTime = str(availableTime)
        cproject.availableTime = newAvailableTime_str
        cuser.save()
        cproject.save()
        return True
