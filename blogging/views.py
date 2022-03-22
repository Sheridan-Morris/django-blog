from typing import List
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.syndication.views import Feed
from django.urls import reverse


class BloggingListView(ListView):
    model = Post
    # queryset = model.objects.filter(published_date__exact != None)
    queryset = model.objects.order_by("-published_date").exclude(published_date=None)
    template_name = "blogging/list.html"


class BloggingDetailView(DetailView):
    model = Post
    template_name = "blogging/detail.html"


class LatestEntriesFeed(Feed):
    title = "Blog RSS"
    link = "/sitenews/"
    description = "Updates on changes and additions to blog."

    def items(self):
        return Post.objects.order_by("-published_date")[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

    def item_link(self, item):
        return reverse("blog_detail", args=[item.pk])
