from django.db import models
from PIL import Image
from django.contrib.auth.models import User
import mutagen
import time

# Create your models here.

def singer_directory_path(instance, filename):
    singer_name = str(instance.singer_name)
    _,ext = filename.split('.')
    timestap = int(time.time()*1000)
    f_name = singer_name + str(timestap)+'.'+ext
    return f'singer/{singer_name}/{f_name}'

class Singer(models.Model):
    '''
    Singer profile model
    '''
    singer_name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = singer_directory_path,default = 'logo/profile.jpg')
    about = models.CharField(max_length = 150)
    def __str__(self) -> str:
        return self.singer_name

    def save(self,*args, **kwargs):
        try:
            prev = Singer.objects.get(id=self.id)
            if prev.image != self.image:
                import os
                if os.path.exists(prev.image.path):
                    print(prev.image.name)
                    os.remove(prev.image.path)
        except:
            pass
        finally:
            super().save(*args, **kwargs)
            c_p = Image.open(self.image)
            c_p.resize((200,200),Image.NEAREST)
            c_p.save(self.image.path)

def album_directory_path(instance, filename):
    album_name = str(instance.album_name)
    _,ext = filename.split('.')
    timestap = int(time.time()*1000)
    f_name = album_name + str(timestap)+'.'+ext
    return f'album/{album_name}/{f_name}'

class Album(models.Model):
    '''
    Album profile model
    '''
    album_name = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = album_directory_path,default = 'logo/profile.jpg')
    singers = models.ManyToManyField(Singer)

    def get_singers(self):
        return ','.join([str(singer) for singer in self.singers.all()])


    def __str__(self) -> str:
        return self.album_name

    def save(self,*args, **kwargs):
        try:
            prev = Album.objects.get(id=self.id)
            if prev.image != self.image:
                import os
                if os.path.exists(prev.image.path):
                    print(prev.image.name)
                    os.remove(prev.image.path)
        except:
            pass
        finally:
            super().save(*args, **kwargs)
            c_p = Image.open(self.image)
            c_p.resize((200,200),Image.NEAREST)
            c_p.save(self.image.path)

def file_directory_path(instance, filename):
    album_name = str(instance.album)
    *_,ext = filename.split('.')
    f_name = instance.song_name +'.'+ext
    return f'music/{album_name}/{f_name}'

class Song(models.Model):
    '''
    Song model stores song and its poperty
    '''
    song_name = models.CharField(max_length = 50)
    album = models.ForeignKey(Album,on_delete = models.CASCADE,null =True,blank = True)
    extension = models.CharField(max_length = 10,blank=True,null=True,editable = False)
    music_file = models.FileField(upload_to=file_directory_path)
    duration = models.CharField(max_length = 50,null=True,blank = True,editable = False)
    liked_by = models.ManyToManyField(User)

    def __str__(self) -> str:
        return self.song_name
    
    def save(self,*arg,**kwarg):
        ln = mutagen.File(self.music_file).info.length
        ln = str(int(ln//3600)) +':'+ str(int((ln - 3600*(ln//3600))//60)) + ':'+str(int(round(ln - (3600*(ln//3600)+ 60*(ln//60)))))
        self.duration = ln
        file_name = self.music_file.name
        *_,ext = file_name.split('.')
        self.extension = ext
        return super().save(*arg,**kwarg)
