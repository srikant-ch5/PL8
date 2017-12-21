from django.db import models
from django.contrib.auth.models import User
import uuid#required for unique instance of video or audio

class Video(models.Model):
    video_title = models.CharField(max_length=250)
    video_logo = models.CharField(max_length=250)
    length = models.IntegerField()

    def __str__(self):
            return self.video_title

    def get_absolute_url(self):
        '''returns the url to access particular video instance'''
        return reverse('video-details',args=[str(self.id)])

class Audio(models.Model):
    audio_title = models.CharField(max_length = 250)
    audio_logo = models.CharField(max_length=250)
    length = models.IntegerField()

    def __str__(self):
        return self.audio_title

class VideoInstance(models.Model):
    '''Model representing particular video copy that is in the users downloadAccount'''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique id for the this video across the videoLibrary")
    video = models.ForeignKey('Video',on_delete=models.SET_NULL,null=True)

    #video status whether the user has access or have downloaded the video
    DOWNLOAD_STATUS = (
        ('d','downloaded'),
        ('n','not Downloaded')
    )

    status = models.CharField(max_length=1,choices=DOWNLOAD_STATUS,blank=True,default = 'n',help_text="video avaibility")
    viewer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    def __str__(self):
        return '%s (%s)' %(self.id,self.video.video_title)

class AudioInstance(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="Unique id for this audio across the AudioLibrary")
    audio = models.ForeignKey('Audio',on_delete = models.SET_NULL,null=True)

    DOWNLOAD_STATUS =(
        ('d','downloaded'),
        ('n','not downloaded')
    )

    status = models.CharField(max_length = 1,choices = DOWNLOAD_STATUS,blank = True,default = 'n',help_text="audio avaibility")
    listener = models.ForeignKey(User,on_delete = models.SET_NULL,null=True)

    def __str__(self):
        return '%s (%s)' %(self.id,self.audio.audio_title)

class Files(models.Model):
    description = models.CharField(max_length= 255,blank = True)
    file = models.FileField(upload_to = 'documents/')
    uploaded_at = models.DateTimeField(auto_now_add = True)
