from django.db import models

# Create your models here.

from django.contrib.auth.models import User


# Create your models here.
class Room(models.Model):
    room_no = models.CharField(max_length=5)
    price = models.PositiveSmallIntegerField()
    availability = models.BooleanField(default=0)
    Date=models.DateField(blank=False)

    class Meta:
        unique_together = ('room_no', 'Date',)





class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    time = models.TimeField()

    def __str__(self):
        return str(self.time)+self.room_no.room_no

