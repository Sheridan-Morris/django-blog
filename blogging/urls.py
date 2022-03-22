from django.urls import path
from blogging.views import BloggingListView, BloggingDetailView
from blogging.views import LatestEntriesFeed

urlpatterns = [
    path("", BloggingListView.as_view(), name="blog_index"),
    path("posts/<int:pk>/", BloggingDetailView.as_view(), name="blog_detail"),
    path("latest/feed/", LatestEntriesFeed()),
]
