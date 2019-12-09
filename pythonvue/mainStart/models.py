from django.db import models

# Create your models here.
class mainStart(models.Model):
    mainStart_id = models.AutoField(primary_key=True)
    mainStart_heading = models.CharField(max_length=250)
    mainStart_body = models.TextField()
