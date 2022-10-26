from post.models import Participation, Project, User, ParticipationDetail
from django.http import HttpResponse

def createUser(userName, userPassword, projectId):
    if userName is not None:
        cuser = User.objects.create(userName=userName, userPassword=userPassword)
        cparticipation = Participation.objects.create(projectId=projectId, userId=cuser.pk)
        cuser.save()
        cparticipation.save()
        return True
    return False

def verifyUserLoginData(projectId, userName, userPassword):
    cparticipation = Participation.objects.filter(projectId=projectId).extra(
        select={'userName': 'user.userName', 'userPassword': 'user.userPassword'},
        tables=['user'],
        where=['participation.userId=user.ID', "user.userName='"+userName+"'", "user.userPassword='"+userPassword+"'"]
    )
    if cparticipation.count() == 0 :
        return False
    else:
        return True

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

def queryUserFromParticipation(projectId):
    cparticipation = Participation.objects.filter(projectId=projectId).extra(
        select={'userName': 'user.userName', 'userPassword': 'user.userPassword'},
        tables=['user'],
        where=['userId=user.ID']
    ).values('id', 'projectId', 'userId', 'userName', 'userPassword')
    return cparticipation