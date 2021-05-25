"""blog_mvc_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from project.Controllers import HomeController, PostController


urlpatterns = [
    path("", HomeController.index, name="home.index"),
    path("about/", HomeController.about, name="home.about"),
    path("posts/", PostController.list, name="posts.list"),
    path("posts/save", PostController.save, name="posts.save"),
    path("posts/saveComment", PostController.saveComment, name="posts.saveComment"),
    path("posts/<int:id>", PostController.show, name="posts.show"),
    path(
        "posts/deleteComment/", PostController.deleteComment, name="posts.deleteComment"
    ),
]
