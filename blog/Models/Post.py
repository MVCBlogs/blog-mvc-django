from django.db import models
from django.core.exceptions import ValidationError

class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def getId(self):
        return self.id

    def getTitle(self):
        return self.title

    def getDescription(self):
        return self.description

    def getCreatedAt(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.updated_at

    def setId(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def setDescription(self, description):
        self.description = description

    def setCreatedAt(self, created_at):
        self.created_at = created_at

    def setUpdatedAt(self, updated_at):
        self.updated_at = updated_at

    def clean(self):
        if not self.title or not self.description:
            raise ValidationError("Title or description cannot be empty")
