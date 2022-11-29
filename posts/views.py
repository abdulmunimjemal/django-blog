from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

class DetailPageView(DetailView):
    model = Post
    template_name = 'detail_view.html'
    context_object_name = 'post'
