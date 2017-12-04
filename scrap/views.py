from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import News, Folder, Folder_News

# Create your views here.
from bs4 import BeautifulSoup
import requests

def login_login(request):
	return render(request, 'scrap/login.html', {})

def login_configure(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = authenticate(request, username = username, password = password)

	if user is not None :
		login(request, user)
		return redirect('/folder/')
	else :
		return redirect('/login/')

def signup_signup(request):
	return render(request, 'scrap/signup.html', {})

def signup(request):
	username = request.POST["username"]
	password = request.POST["password"]
	user = User.objects.create_user(username = username, password = password)
	user.save()
	login(request, user)
	return redirect('/folder')

def folder_list(request):
	if request.user.is_authenticated():
		new_folder = request.POST.get('folderName', 0)
		if new_folder is not 0:
			folder = Folder(userId = request.user, folderName = request.POST["folderName"])
			folder.save()
		folder = Folder.objects.filter(userId = request.user)
		return render(request, 'scrap/folder_list.html', {'folders' : folder} )
	else:
		return redirect('/login/')

def news_list(request, store_id):
	context = {}
	folder_number = store_id
	new_news = request.POST.get('url', 0)
	folder = Folder.objects.filter(folderNumber = store_id).first()
	if new_news is not 0:
		response = requests.get(request.POST["url"])
		soup = BeautifulSoup(response.text)
		for a in soup.findAll('a'):
			try:
				if "http" not in a['href']:
					index = request.POST["url"].find('com')
					a['href'] = request.POST["url"][:index + 3] + a['href']
			except KeyError:
				pass
		news = News(userId = request.user, newsName = request.POST["title"], newsFile = str(soup))
		news.save()
		folder_news = Folder_News(folderNumber = folder, newsNumber = news)
		folder_news.save()
	folder_news = Folder_News.objects.filter(folderNumber = folder)

	context["folder_news"] = folder_news
	context["folder"] = store_id
	return render(request, 'scrap/news_list.html', context)

