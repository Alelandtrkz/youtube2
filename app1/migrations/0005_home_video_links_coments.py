# Generated by Django 4.2.2 on 2024-05-30 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_remove_video_page_links_likes_home_video_links_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_video_links',
            name='coments',
            field=models.TextField(default='algun comentatior', verbose_name='coments'),
        ),
    ]
