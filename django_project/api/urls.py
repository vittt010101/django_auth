# accounts/urls.py
from django.urls import path

from .views import PostList
from .views import CommentList
from .views import ReactionList


urlpatterns = [
    path("posts/", PostList.as_view(), name="posts"),
    path("comments/", CommentList.as_view(), name="comments"),
    path("reactions/", ReactionList.as_view(), name="reactions"),
]