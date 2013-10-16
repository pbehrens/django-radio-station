from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.
fs = FileSystemStorage(location="/Users/thebeagle/dev/django/wluwmodules/wluwmodules/media/coverimages")


class Post(models.Model):
	title = models.CharField(max_length=300)
	post = models.TextField(max_length=200000)
	pub_date = models.DateTimeField('date published', null = True, blank= True)
	coverImage = models.ImageField(upload_to="coverimages", null = True, blank= True)
	
	def __str__(self):
	        return self.title
	
	class Admin:
	  list_display = ('title', 'date' )
	  search_fields = ('title', 'post')
	

	
	