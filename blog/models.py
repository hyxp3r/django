from tabnanny import verbose
from django.utils import timezone
from django.conf import settings
from django.db import models



class Post(models.Model):

    '''Post tabe'''

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, verbose_name = 'Автор')
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self) -> str:

        return self.title
    
