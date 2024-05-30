from django.db import models
from django.contrib.auth.models import User

class home_video_links(models.Model):
    title = models.CharField('title',max_length=80)
    user = models.CharField('user',max_length=80)
    photo = models.TextField('photo', default='SOME STRING')
    date = models.TextField('date', default='YYYY-MM-DD')
    video = models.TextField('video', default='SOME STRING')
    coments = models.TextField('coments', default='algun comentatior')
    likes = models.ManyToManyField(User, related_name='likes')

    def cantidad_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title

    class Meta:
        verbose_name: 'Description of the video'
        verbose_name_plural: 'Add description'

class video_page_links (models.Model):
    main_video = models.TextField('main_video',default='link')
    video_1 = models.TextField('video1',default='link')
    video_2 = models.TextField('video2', default='link')
    video_3 = models.TextField('video3', default='link')
    video_4 = models.TextField('video4', default='link')
    video_5 = models.TextField('video5', default='link')



class table_user (models.Model):
    usuario = models.TextField('usuario', default='user')
    email = models.TextField('email', default='email')
    password = models.TextField('password', default='password')