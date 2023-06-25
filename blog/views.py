from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import Post
from django.utils import timezone
# Create your views here.

def bomba(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    print(posts)

    return render(request, 'blog/index.html', {"posts":posts})
