from django.db import models


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    postReference = models.ForeignKey("Post", on_delete=models.CASCADE)
    message = models.CharField(max_length=110)
    date = models.DateTimeField(auto_now_add=True)

    def getId(self):
        return self.id

    def getPostId(self):
        return self.postReference

    def getMessage(self):
        return self.message

    def getDate(self):
        return self.date

    def setId(self, id):
        return self.id == id

    def setPostId(self, post):
        return self.post == post

    def setMessage(self, message):
        return self.message == message

    def setDate(self, date):
        return self.date == date
