from django.db import models
from django.core.files.storage import FileSystemStorage
from sorl.thumbnail import get_thumbnail
from sorl.thumbnail import ImageField
import os
from django.conf import settings


# Create your models here.
# fs = FileSystemStorage(location= )

def get_upload_path(instance, filename):
    return os.path.join("user_%d" % instance.owner.id, "car_%s" % instance.slug, filename)

class Post(models.Model):
    title = models.CharField(max_length=300)
    post = models.TextField(max_length=200000)
    pub_date = models.DateTimeField('date published', null = True, blank= True)
    coverImage = models.ImageField(upload_to="upload/", null = True, blank= True)
    thumbnail = models.ImageField(upload_to= "upload/", null = True, blank = True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # self.thumbnail = get_thumbnail(self.coverImage, '73x42', crop='center', quality=99) 
        super(Post, self).save(*args, **kwargs) # Call the "real" save() method.

    def __str__(self):
            return self.title
    
    class Admin:
      list_display = ('title', 'date' )
      search_fields = ('title', 'post')
    


    
    