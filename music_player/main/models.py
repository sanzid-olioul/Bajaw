from django.db import models
import mutagen
# Create your models here.
class Singer(models.Model):
    singer_name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'singer/',blank = True,null = True)
    about = models.CharField(max_length = 150)
    def __str__(self) -> str:
        return self.singer_name


class Album(models.Model):
    album_name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'singer/',blank = True,null = True)
    singer = models.ForeignKey(Singer,on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.album_name

class Songs(models.Model):
    song_name = models.CharField(max_length = 50)
    EX = [
        ('mp3','mp3'),
        ('wav','wav'),
        ('wma','wma'),
        ('m4a','m4a'),
    ]
    album = models.ForeignKey(Album,on_delete = models.CASCADE,null =True,blank = True)
    extension = models.CharField(max_length=4,choices = EX)
    music_file = models.FileField(upload_to='music/')
    duration = models.CharField(max_length = 50,null=True,blank = True,editable = False)

    def __str__(self) -> str:
        return self.song_name
    
    def save(self,*arg,**kwarg):
        ln = mutagen.File(self.music_file).info.length
        ln = str(int(ln//3600)) +':'+ str(int((ln - 3600*(ln//3600))//60)) + ':'+str(int(round(ln - (3600*(ln//3600)+ 60*(ln//60)))))
        self.duration = ln
        return super().save(*arg,**kwarg)
