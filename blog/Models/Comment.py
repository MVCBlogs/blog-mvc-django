from django.db import models
from django.core.exceptions import ValidationError

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.CharField(max_length=110)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')

    def getId(self):
        return self.id

    def getMessage(self):
        return self.message

    def getCreatedAt(self):
        return self.created_at

    def getUpdatedAt(self):
        return self.updated_at

    def getPostId(self):
        return self.post_id

    def setId(self, id):
        self.id = id

    def setMessage(self, message):
        self.message = message

    def setCreatedAt(self, created_at):
        self.created_at = created_at

    def setUpdatedAt(self, updated_at):
        self.updated_at = updated_at

    def setPostId(self, post_id):
        self.post_id = post_id

    def clean(self):
        if not self.message:
            raise ValidationError("Message cannot be empty")
