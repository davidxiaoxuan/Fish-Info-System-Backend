from django.db import models

class Fish(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
