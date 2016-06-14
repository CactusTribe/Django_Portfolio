from django.shortcuts import render
from django.http import HttpResponse, Http404
from home.models import Categorie, Project, Image, Resource, IconFile

import subprocess

def home(request, langue="fr"):
	projects = Project.objects.all().order_by("date")
	images = Image.objects.all()
	resources = Resource.objects.all()
	iconsfiles = IconFile.objects.all()
	categories = Categorie.objects.all()

	if langue == "fr" :
		subprocess.Popen(["python3","/home/pi/pyprojects/Divers/LED_RGB.py", "40", "178", "135"])
	else:
		subprocess.Popen(["python3","/home/pi/pyprojects/Divers/LED_RGB.py", "190", "20", "24"])

	return render(request, 'index.html', locals())