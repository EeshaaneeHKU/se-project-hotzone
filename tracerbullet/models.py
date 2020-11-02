from django.db import models

class UserDetails(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30, default="")
    x_coordinate = models.IntegerField(default=0)
    y_coordinate = models.IntegerField(default=0)
    #date_present = models.DateTimeField()
    #category_location = CharField(max_length=30)

    def __str__(self):
        return self.name