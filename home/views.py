from django.shortcuts import render
from django.http import HttpResponse, Http404
from home.models import Categorie, Project, Image, Resource, IconFile

from home.LED_RGB import LED_RGB
import RPi.GPIO as GPIO

def home(request, langue="fr"):
	projects = Project.objects.all().order_by("date")
	images = Image.objects.all()
	resources = Resource.objects.all()
	iconsfiles = IconFile.objects.all()
	categories = Categorie.objects.all()

	led1 = LED_RGB(1, 22,27,17)

	if langue is "fr":
		led1.setColor_RGB(40, 178, 135)
	else:
		led1.setColor_RGB(170, 78, 115)

	led1.blink(2)

	return render(request, 'index.html', locals())