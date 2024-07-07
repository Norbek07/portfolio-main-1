from django.db import models
from ckeditor.fields import RichTextField

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} {self.email}"


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.name}"
    
class Blog(models.Model):
    title = models.CharField(max_length=100)
    # slug = models.SlugField()
    image = models.ImageField(upload_to='Blogs/images')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_date = models.DateField(auto_now=True)
    author = models.CharField(max_length=50)
    content = RichTextField()
    def __str__(self):
        return f"{self.title} by {self.author}"
