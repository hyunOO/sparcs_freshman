from django.db import models

# Create your models here.

class News(models.Model):
	userId = models.ForeignKey('auth.User')
	newsNumber = models.AutoField(primary_key = True)
	newsName = models.CharField(unique = True, max_length = 20)
	newsFile = models.TextField()

class Folder(models.Model):
	userId = models.ForeignKey('auth.User')
	folderNumber = models.AutoField(primary_key = True)
	folderName = models.CharField(unique = True, max_length = 20)

class Folder_News(models.Model):
	newsNumber = models.ForeignKey('scrap.News', on_delete = models.CASCADE)
	folderNumber = models.ForeignKey('scrap.Folder', on_delete = models.CASCADE)