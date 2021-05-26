from django.shortcuts import render

def index(request):
    data = {}
    data["title"] = "Blog - Django"
    data["description"] = "A clean blog with an MVC architecture in Django"
    return render(request, "home/index.html", {"data": data})

def about(request):
    data = {}
    data["title"] = "About us"
    data["description"] = "Information about the developers of this application"
    return render(request, "home/about.html", {"data": data})
