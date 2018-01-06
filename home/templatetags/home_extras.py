from django import template

register = template.Library()

@register.filter
def getImagesProject(images, id_project):
	return images.filter(project=id_project)

@register.filter
def getResourcesProject(resources, id_project):
	return resources.filter(project=id_project)
