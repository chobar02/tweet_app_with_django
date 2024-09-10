from django.urls import path
from . import views

urlpatterns = [
    path("", views.tweet_list, name="tweet_list"),
    path("create/", views.tweet_create, name="tweet_create"),
    path("<int:tweet_id>/edit/", views.tweet_edit, name="tweet_edit"),
    path("<int:tweet_id>/delete/", views.tweet_delete, name="tweet_delete"),
    path("search/", views.tweet_search, name="tweet_search"),
    path("register/", views.register, name="register"),
    path("user_logout/", views.user_logout, name="user_logout"),
]