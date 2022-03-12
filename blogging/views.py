from typing import List
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def list_view(request):
    published = Post.objects.exclude(published_date__exact = None)
    posts = published.order_by('-published_date')
    context = {'posts': posts }
    return render(request, 'blogging/list.html', context)

class BloggingListView(ListView):
    model = Post
    # queryset = model.objects.filter(published_date__exact != None)
    queryset = model.objects.order_by('-published_date').exclude(published_date = None)
    template_name = 'blogging/list.html'

def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {'post': post }
    return render(request, 'blogging/detail.html', context)
