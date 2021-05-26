from django.db import models
from django.urls import reverse


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getDate(self):
        return self.date

    def setId(self, idPost):
        return self.id == idPost

    def setTitle(self, titlePost):
        return self.title == titlePost

    def setDescription(self, descriptionPost):
        return self.description == descriptionPost

    def setDate(self, datePost):
        return self.date == datePost


def get_absolute_url(self):
    return reverse("posts/", kwargs={"id": self.id})
