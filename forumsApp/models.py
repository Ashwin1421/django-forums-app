from django.db import models

# Create your models here.

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    content = models.TextField()
    article_image = models.ImageField(upload_to='uploads/',default='noimage.png')
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=150)

    def __str__(self):
        return self.title
