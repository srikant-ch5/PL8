from django.contrib import admin
from .models import Video,Audio,VideoInstance,AudioInstance

# Register your models here.
admin.site.register(Video)
admin.site.register(Audio)

@admin.register(VideoInstance)
class VideoInstanceAdmin(admin.ModelAdmin):
    list_display = ('video','status','viewer','id')

    fieldsets =  (
        (None,{
            'fields' : ('video','id')
        }),
        ('Avaibility',{
            'fields' : ('status','viewer')
        })
    )

@admin.register(AudioInstance)
class AudioInstance(admin.ModelAdmin):
    list_display = ('audio','status','listener','id')

    fielsets = (
        (None,{
            'fields' : ('audio','listener')
        }),
        ('Avaibility',{
            'fields' : ('status','listener')
        })
    )
