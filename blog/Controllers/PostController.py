from django.shortcuts import render, redirect
from blog.Models.Post import Post
from blog.Models.Comment import Comment
from django.contrib import messages

def list(request):
    data = {}
    data["title"] = "Posts"
    data["description"] = "List of Posts"
    data["posts"] = Post.objects.all()
    return render(request, "post/list.html", {"data": data})

def show(request, id):
    data = {}
    post = Post.objects.get(id=id)

    data["title"] = post.getTitle
    data["description"] = post.getDescription
    data["post"] = post

    return render(request, "post/show.html", {"data": data})

def save(request):
    if request.method == "POST":
        newPost = Post()
        newPost.setTitle(request.POST.get("title"))
        newPost.setDescription(request.POST.get("description"))
        newPost.clean()
        newPost.save()
        messages.success(request, "Post created sucessfully!")
        return redirect("/posts")
    else:
        return redirect("/posts")

def saveComment(request):
    if request.method == "POST":
        post = Post.objects.get(id=request.POST.get("post_id"))
        newComment = Comment()
        newComment.post = post
        newComment.setMessage(request.POST.get("message"))
        newComment.clean()
        newComment.save()
        messages.success(request, "Comment created successfully!")
    return redirect("/posts/"+request.POST.get("post_id"))

def deleteComment(request):
    comment_id = request.POST.get("comment_id")
    post_id = request.POST.get("post_id")
    comments = Comment.objects.get(id=comment_id)
    comments.delete()
    return redirect("/posts/"+post_id)
