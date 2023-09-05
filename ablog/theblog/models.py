from django.db import models
from django.contrib.auth.models import User #user
from django.urls import reverse
from datetime import date, datetime
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Follow(models.Model):
    follower = models.ForeignKey(User, related_name="following", on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.follower} follows {self.following}"

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name 
    
    def get_absolute_url(self):
        return reverse("post:home")

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE) #One to One profile.user > User
    profile_pic = models.ImageField(null=True,blank=True, upload_to="members/images/profile/")
    follower = models.ManyToManyField(User,related_name="follows")

    def total_followers(self):
        return self.follower.count()
 
    def __str__(self):
        return str(self.user) 
    
    def follow(self, profile):
        Follow.objects.create(follower=self.user, following=profile.user)
        
    def unfollow(self, profile):
        Follow.objects.filter(follower=self.user, following=profile.user).delete()
    
    def get_absolute_url(self):
        return reverse("post:home")
    

class Post(models.Model): #1
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # delete all the blogpost of a user when user is deleted
    category = models.CharField(max_length=255,default='coding')
    body = RichTextField(blank=True, null=True)
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse("post:home")
    
    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE) #1
    name = models.CharField(max_length=255) #User
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' %(self.post.title, self.name)
    
