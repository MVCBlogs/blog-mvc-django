from django.db import models
from django.core.exceptions import ValidationError

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

    def setId(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def setDescription(self, description):
        self.description = description

    def setDate(self, date):
        self.date = date

    def clean(self):
        if not self.title or not self.description:
            raise ValidationError("Title or description cannot be empty")
