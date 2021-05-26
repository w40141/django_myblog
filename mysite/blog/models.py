from django.db import models

# Create your models here.


class Post(models.Model):
    """Post class"""

    title = models.CharField(
        "Title ",
        max_length=100,
    )
    body = models.TextField("Content")
    created_at = models.DateTimeField(
        "Date ",
        auto_now_add=True,
    )
