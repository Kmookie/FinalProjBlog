from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models



@python_2_unicode_compatible  # only if you need to support Python 2
class Post(models.Model):
    
    title = models.CharField(max_length=100)
    body = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body