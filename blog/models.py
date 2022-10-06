from pyexpat import model
from tokenize import blank_re
from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # user = models.ForeignKey(User, related_name='categoryuser', on_delete=models.CASCADE, blank=True, null=True)
    user = models.ManyToManyField(User, blank=True, null=True)

    def __str__(self):
        return self.name

class Post(models.Model):

    title = models.CharField(max_length=60)
    image = models.ImageField(blank=True, null=True)
    content = models.CharField(max_length=255)
    category = models.ForeignKey('Category', related_name='posts', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='postuser', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    likes = models.IntegerField(blank=True, null=True)
    dislikes = models.IntegerField(blank=True, null=True)



    def __str__(self):
        return self.title

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):

    content = models.CharField(max_length=255)
    post = models.ForeignKey('Post', related_name='commentpost', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'

class Reply(models.Model):

    content = models.CharField(max_length=255)
    comment = models.ForeignKey('Comment', related_name='commentreply', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, related_name='userreply', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'reply'
        verbose_name_plural = 'reply'

class BadWord(models.Model):

    word = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    user = models.ForeignKey(User, related_name='badwords', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.word

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'bad_word'
        verbose_name_plural = 'bad_word'





