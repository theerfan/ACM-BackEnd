from django.db import models
from django.core.validators import ValidationError

# Create your models here.


class TimeLineItem(models.Model):
    dateText = models.TextField()
    style = models.TextField()
    dateInnerStyle = models.TextField()
    title = models.TextField()
    innerHTML = models.TextField()

    def __str__(self):
        return self.title


class Countdown(models.Model):
    stopTime = models.DateTimeField()

    def __str__(self):
        return "Homepage countdown time"

    def save(self, *args, **kwargs):
        if Countdown.objects.exists() and not self.pk:
            raise ValidationError('There can be only one Countdown')
        return super(Countdown, self).save(*args, **kwargs)


# class Contest(models.Model):
#     date = models.DateField()
#     title = models.TextField()

#     def __str__(self):
#         return self.title


# class ContestImage(models.Model):
#     imageFile = models.ImageField(upload_to="")
#     contest = models.ForeignKey(Contest, on_delete=None)
#     caption = models.TextField(default="")
#     #

#     def __str__(self):
#         return self.caption
        
# class MainContest(models.Model):
#     pass
