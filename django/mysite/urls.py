"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from post.views import PostFillOutForm, RegisterProject,\
    createProject, createUser, userLogin,\
    updateUserAvailableTime, getAllAvailableTime_user, getAllAvailableTime_project


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RegisterProject.as_view()),
    path('<pk>', PostFillOutForm.as_view(), name="PostFillOutForm"),
    path('createProject/', createProject),
    path('createUser/', createUser),
    path('userLogin/', userLogin),
    path('updateUserAvailableTime/', updateUserAvailableTime),
    path('getAllAvailableTime_user/', getAllAvailableTime_user),
    path('getAllAvailableTime_project/', getAllAvailableTime_project)
]
