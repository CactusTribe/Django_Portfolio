from django.db import models

class Categorie(models.Model):
	nom = models.CharField(max_length=30)
	nom_traduction = models.CharField(max_length=30, null=True)

	def __unicode__(self):
		return self.nom

class Tool(models.Model):
	nom = models.CharField(max_length=30)
	icon = models.ImageField(upload_to="icons_tools/")

	def __unicode__(self):
		return self.nom

class Project(models.Model):
	titre = models.CharField(max_length=100)
	titre_traduction = models.CharField(max_length=100, null=True)
	contenu = models.TextField(null=True)
	contenu_traduction = models.TextField(null=True)
	date_realisation = models.TextField(null=True)
	date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date de parution")
	categories = models.ManyToManyField(Categorie)
	tools = models.ManyToManyField(Tool)

	def __unicode__(self):
		return self.titre

class Image(models.Model):
	titre = models.CharField(max_length=100)
	description = models.TextField(null=True, max_length=250)
	description_traduction = models.TextField(null=True, max_length=250)
	img = models.ImageField(upload_to="images/")
	project = models.ForeignKey(Project)

	def __unicode__(self):
		return self.titre

class IconFile(models.Model):
	nom = models.CharField(max_length=30)
	icon = models.ImageField(upload_to="icons_files/")

	def __unicode__(self):
		return self.nom

class Resource(models.Model):
	nom = models.CharField(max_length=30)
	version = models.CharField(max_length=30)
	fichier = models.FileField(upload_to="resources/")
	type = models.ForeignKey(IconFile)
	project = models.ForeignKey(Project)

	def __unicode__(self):
		return self.nom


