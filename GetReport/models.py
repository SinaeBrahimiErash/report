from django.db import models


# Create your models here.
class report(models.Model):
    organization = models.CharField(max_length=500,)
    centername = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    subject = models.TextField()
    description = models.TextField()
    oncall = models.BooleanField(default=False)

    def __str__(self):
        return self.centername
