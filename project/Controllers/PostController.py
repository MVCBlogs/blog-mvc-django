from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from project.Models.Post import Post
from project.Models.Comment import Comment
from django.contrib import messages
from django.http import Http404
from django.urls import reverse
from django.shortcuts import get_object_or_404


def list(request):
    data = {}
    data["title"] = "Posts"
    data["description"] = "List of Posts"
    data["posts"] = Post.objects.all()
    return render(request, "post/list.html", {"data": data})


def show(request, id):
    # Pendiente por modificar
    data = {}
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(postReference_id=id)

    data["title"] = post.getTitle
    data["description"] = post.getDescription
    data["post"] = post
    data["comments"] = comments

    return render(request, "post/show.html", {"data": data})


def save(request):
    if request.method == "POST":
        if request.POST.get("title") and request.POST.get("description"):
            newPost = Post()
            newPost.title = request.POST.get("title")
            newPost.description = request.POST.get("description")
            newPost.save()
            messages.success(request, "Post created sucessfully!")
            return redirect("/posts")
    else:
        return redirect("/posts")


def saveComment(request):
    if request.method == "POST":
        if request.POST.get("message") and request.POST.get("postReference_id"):
            newComment = Comment()
            newComment.postReference = request.POST.get("postReference_id")
            newComment.message = request.POST.get("message")
            newComment.save()
            messages.success(request, "Comment created successfully!")
            return redirect("/posts")
    else:
        return redirect("/posts")


def deleteComment(request, id):
    comments = Comment.objects.get(id=id)
    comments.delete()
    return redirect("/")
