from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostFillOutForm(DetailView):
    model = Post
    template_name = 'post_userForm.html'

class RegisterProject(ListView):
    model = Post
    template_name = 'post_register.html'
