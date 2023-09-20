from django.db import models
from django.contrib.auth.models import User
 
from ckeditor.fields import RichTextField

class MyModel(models.Model):
    content = RichTextField()

# Create your models here.
class Features(models.Model):
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    
    
    def __str__(self):
        return f'{self.title} - {self.description}'
    
class Category(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    image = models.FileField(upload_to='categoies/image')
    
    def __str__(self):
        return  self.title
time_of_work = (
    ( "on site" , "on site"),
    ("remotly " , "remotly "),
    ("other" , "other"),
)

type_of_work = {
    ("full time" , "full time"),
    ("part time" , "part time"),
    ("by taske" , "by taske"),
    ("other" , "other"),
    }
  
class Jobs(models.Model):
    auther = models.ForeignKey(User , on_delete=models.PROTECT ,blank=True, null=True ) 
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=5000)
    category = models.ForeignKey(Category , on_delete=models.PROTECT )
    country = models.CharField(max_length=15,blank=True, null=True)
    cite = models.CharField(max_length=15,blank=True, null=True)
    image = models.FileField(upload_to="jobs/image" , default='img\post.png')
    content = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    trend = models.BooleanField(default=True)
    approve = models.BooleanField(default=False)
    link = models.URLField(blank=True, null=True)
    applyed = models.BooleanField(default=False)
    type = models.CharField(max_length=50 , choices=type_of_work  ,default="fulltime")
    time = models.CharField(max_length=50 , choices=time_of_work  ,default="on site")
    slary = models.IntegerField(blank=True, null=True)
    location = models.URLField(blank=True, null=True , default='world')
    tage = models.CharField(max_length=100, blank=True, null=True )
    number_of_view = models.IntegerField(default=0)
    rating = models.IntegerField(default=0)
    
    
    def __str__(self):
        return f"{self.title} - {self.description[0:15]}"
    
class Profile(models.Model):
    user = models.OneToOneField(User , related_name='User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/profiles')
    cover = models.ImageField(upload_to='profile/covers')
    location = models.URLField()
    campany = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.user.username} - {self.campany}'
    
    
    
    
    
    
    