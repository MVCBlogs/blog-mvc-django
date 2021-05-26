from django.db import models
from django.core.exceptions import ValidationError

class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.CharField(max_length=110)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name='comments')

    def getId(self):
        return self.id

    def getMessage(self):
        return self.message

    def getDate(self):
        return self.date

    def getPostId(self):
        return self.post_id

    def setId(self, id):
        self.id = id

    def setMessage(self, message):
        self.message = message

    def setDate(self, date):
        self.date = date

    def setPostId(self, post_id):
        self.post_id = post_id

    def clean(self):
        if not self.message:
            raise ValidationError("Message cannot be empty")
