from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Video,Audio,VideoInstance,AudioInstance,Files
from .forms import FileForm
from django import forms


import subprocess
import pafy
import json
import os
import urllib
from urllib.request import urlopen
from urllib.parse import parse_qs

@login_required
def index(request):
	'''View function for the homepage of the site'''
	#Calculate the sum of all the videos from Video
	num_videos = Video.objects.all().count()
	num_videoInstances = VideoInstance.objects.all().count()

	return render(request,'youtubeadl/home.html')

def submit(request):
	if request.method == "POST":
		try:
			url = request.POST.get("link",False)
			yv_video = pafy.new(url)
			title = yv_video.title
			length = yv_video.length
			user = request.user
			streams = yv_video.streams
			best_quality = yv_video.getBest()
			
			best_quality.download(quiet = False)
		
			present = False
			entries = Video.objects.all()

			for i in entries:
				if i.video_title == title:
					present = True

			#code to save the video informantion into the database
			#store videoinfo in all videos
			store_video_all = Video(video_title = title,video_logo = title + "-logo",length = length)
			store_video_useraccount = VideoInstance(video=store_video_all,status='d',viewer = User.objects.get(username=user))
			if present == False:
				store_video_all.save()
				#store videoinfo in user account
				#creating the User instance
				store_video_useraccount.save()
			else:
				store_video_useraccount.save()

			videoInfo  = {
				'title' : title,
				'length':length,
				'user'  :user,
				'avaibility':present
			}

			return render(request,'youtubeadl/download.html',{'succcessStatus':True,'videoInfo':videoInfo})
		except ValueError as e:
			return render(request,'youtubeadl/download.html',{'succcessStatus':False,'error':e})

def download(request):
	return render(request,'youtubeadl/download.html')

class userVideosView(LoginRequiredMixin,ListView):
	"Generic class based views showing the user videos"

	model = VideoInstance #in the template its going to use this model and creates a list as videoinstance_list'''
	template_name = 'youtubeadl/myVideos.html'
	paginate_by = 10

	def get_queryset(self):
		return VideoInstance.objects.filter(viewer=self.request.user).filter(status__exact = 'd').order_by('id')

class userAudiosView(LoginRequiredMixin,ListView):

	model = AudioInstance
	template_name = 'youtubeadl/myAudios.html'
	paginate_by = 10

	def get_queryset(self):
		return AudioInstance.objects.filter(listener = self.request.user).filter(status__exact = 'd').order_by('id')

def models_form_upload(request):
	if request.method == 'POST':
		form = FileForm(request.POST,request.FILES)

		if form.is_valid():
			form.save()
			return redirect('None')
	else:
		form = FileForm()

	return render(request, 'youtubeadl/myfiles.html',{'form' :form})

