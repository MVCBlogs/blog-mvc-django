from django.urls import path
from .Controllers.HomeController import HomeController
from .Controllers.PostController import PostController

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