# Generated by Django 3.2 on 2021-04-14 03:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_music_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='singer',
            field=models.TextField(default='AKB48', help_text='歌手'),
        ),
        migrations.AlterField(
            model_name='music',
            name='song',
            field=models.TextField(default='song', help_text='歌曲名', verbose_name='歌曲'),
        ),
    ]
