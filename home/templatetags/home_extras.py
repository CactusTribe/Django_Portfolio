from django import template

register = template.Library()

@register.filter
def getImagesProject(images, id_project):
	return images.filter(project=id_project)