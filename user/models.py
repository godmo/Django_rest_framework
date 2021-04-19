from django.db import models

# Create your models here.
class Music(models.Model):
    id = models.AutoField(primary_key=True)
    song = models.TextField(default="song", verbose_name="歌曲", help_text="歌曲名")
    singer = models.TextField(default="AKB48", help_text="歌手")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.TextField(default="", help_text="作者")
    title = models.TextField(default="", help_text="書名")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "book"