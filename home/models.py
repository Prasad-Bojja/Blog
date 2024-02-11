from django.db import models
from authentication.models import CustomUser
from tinymce.models import HTMLField
from .helper import generate_slug

class BlogModel(models.Model):
    title = models.CharField(max_length=1000)
    content = HTMLField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)
    user = models.ForeignKey(CustomUser, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog_image')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
