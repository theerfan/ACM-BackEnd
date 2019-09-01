from django.db import models
from django.contrib.postgres.fields import ArrayField



class image(models.Model):
    src = models.CharField(max_length = 500)
    thumbnail = models.CharField(max_length = 500)
    thumbnailheight = 300   
    thumbnailwidth = 400





class ACM (models.Model):
    title = models.CharField(max_length=500)
    problems = models.CharField(max_length=500) 
    final_ranking_onsite = models.CharField(max_length=500)
    final_ranking_online = models.CharField(max_length=550)
    poster = models.CharField(max_length= 500,blank=True, null=True)
    images = models.ForeignKey(image, blank=True, null=True, on_delete=models.CASCADE)




    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'CONTEST'
        verbose_name_plural = 'CONTESTS'    

