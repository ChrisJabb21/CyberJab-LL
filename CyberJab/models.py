from django.db import models
from django.contrib.auth.models import User


#tuple of post status
STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts')
    slug = models.SlugField(max_length=200, unique=True)
    created_date = models.DateTimeField(auto_now = True)
    content = models.TextField()

    status = models.IntegerField(choices=STATUS, default = 0)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

#TODO install taggit and make a WYSIWYG Editor for blog.
#tags
# class Category(models.Model):
 #   title = models.CharField(max_length=250)
