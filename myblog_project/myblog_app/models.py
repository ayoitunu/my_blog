from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

# the foreign key is from a column in superuser table created by django when we migrated
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

# The publish method is to know the time the post was published
    def publish(self):
        self.published_date = timezone.now()
        self.save()

# The method is to show the title of the post and return all data
    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('myblog_app.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)


