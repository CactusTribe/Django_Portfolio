from django.shortcuts import render
from django.http import HttpResponse, Http404
from home.models import Categorie, Project, Image, Resource, IconFile

from subprocess import call

def home(request, langue="fr"):
	projects = Project.objects.all().order_by("date")
	images = Image.objects.all()
	resources = Resource.objects.all()
	iconsfiles = IconFile.objects.all()
	categories = Categorie.objects.all()

	if langue == "fr" :
		call(["py", "~/pyprojects/Divers/main.py"])
	else:
		call(["py", "~/pyprojects/Divers/main.py"])

	return render(request, 'index.html', locals())