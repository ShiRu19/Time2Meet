from contextlib import redirect_stderr, redirect_stdout
from urllib import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import redirect
from .models import Post
#from django.http import HttpResponse

class PostFillOutForm(DetailView):
    model = Post
    template_name = 'post_userForm.html'

class RegisterProject(ListView):
    model = Post
    template_name = 'post_register.html'

def submit(request):
    projectName = request.POST.get('projectName')
    if projectName is not None:
        cuser = Post.objects.create(projectName=projectName)
        cuser.save()
        return redirect("PostFillOutForm", pk=cuser.pk)
