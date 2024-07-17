from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Book(models.Model):
    auther=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    title=description = models.CharField(max_length=100 ,blank=False,null=False)
    description=models.TextField()
    rating=models.IntegerField()
    publish_date=models.DateField()


    ## to rename the the column name in the database
    def __str__(self):
        return self.title