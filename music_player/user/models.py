from django.db import models
from django.contrib.auth.models import User
from main.models import Songs
from PIL import Image
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    cover_photo = models.ImageField(upload_to='Cover',default = '/logo/cover.png')
    profile_photo = models.ImageField(upload_to='Profile',default = '/logo/profile.jpg')
    liked_song = models.ForeignKey(Songs,on_delete = models.CASCADE,null = True,blank = True)
    USER_TYPE_LIST = [
        ('Pri','Premium'),
        ('Reg','Regular'),
    ]
    user_type = models.CharField(choices=USER_TYPE_LIST,max_length = 4,default= 'Reg')

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args, **kwargs):
        try:
            tst = Profile.objects.get(id=self.id)
            if tst.cover_photo != self.cover_photo:
                print(tst.cover_photo.name)
                import os
                if os.path.exists(tst.cover_photo.path):
                    os.remove(tst.cover_photo.path)
            if tst.profile_photo != self.profile_photo:
                print(tst.profile_photo.name)
                import os
                if os.path.exists(tst.profile_photo.path):
                    os.remove(tst.profile_photo.path)
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