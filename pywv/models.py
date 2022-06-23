from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from  ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):
    title=models.CharField(max_length=255)
    header_image=models.ImageField(null=True, blank=True, upload_to='images')
    title_tag=models.CharField(max_length=255, )
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    body=RichTextUploadingField(blank=True,null=True)
    date_created=models.DateField(auto_now_add=True)
    snippet=models.CharField(max_length=255)   

    def __str__(self):
        return self.title + '|' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('allPosts')
    
class Comment(models.Model):
    post=models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name=models.CharField(max_length=255)
    body=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)