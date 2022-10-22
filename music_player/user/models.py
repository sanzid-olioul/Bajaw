from enum import unique
from django.db import models
from django.contrib.auth.models import User
from main.models import Songs
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True,on_delete = models.CASCADE)
    cover_photo = models.ImageField(upload_to='Cover')
    profile_photo = models.ImageField(upload_to='Profile')
    liked_song = models.ManyToManyField(Songs,null = True,blank = True)
    USER_TYPE_LIST = [
        ('Pri','Premium'),
        ('Reg','Regular'),
    ]
    user_type = models.CharField(choices=USER_TYPE_LIST,max_length = 4,default= 'Reg')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        try:
            prev = Profile.objects.get(id=self.id)
            if prev.cover_photo != self.cover_photo:
                import os
                if os.path.exists(prev.cover_photo.path):
                    print(prev.cover_photo.name)
                    os.remove(prev.cover_photo.path)
            if prev.profile_photo != self.profile_photo:
                
                import os
                if os.path.exists(prev.profile_photo.path):
                    print(prev.profile_photo.name)
                    os.remove(prev.profile_photo.path)
        except:
            pass
        finally:
            super().save(*args, **kwargs)
            c_p = Image.open(self.cover_photo)
            p_p = Image.open(self.profile_photo)

            # cp_w ,cp_h = c_p.size
            # pp_w ,pp_h = p_p.size
            c_p.resize((744,200),Image.NEAREST)
            p_p.resize((150,150),Image.NEAREST)
            c_p.save(self.cover_photo.path)
            p_p.save(self.profile_photo.path)