from django.db import models

# Create your models here.


class TextImage(models.Model):
    text = models.ImageField(max_length=512)

    def __str__(self):
        return self.text