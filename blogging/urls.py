from django.urls import path
from blogging.views import BloggingListView, list_view ,detail_view

urlpatterns = [
    path('', BloggingListView.as_view(), name='blog_index'),
    path('posts/<int:post_id>/', detail_view, name='blog_detail')
]