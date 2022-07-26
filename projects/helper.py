from .models import Tag,Project
from django.db.models import Q


def searchProjects(request):
    search_query = ''
    

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    tags = Tag.objects.filter(name__icontains=search_query)
    project = Project.objects.distinct().filter(
        Q(title__icontains = search_query) |
        Q(descripition__icontains = search_query) |
        Q(owner__name__icontains = search_query) |
        Q(tags__in = tags)
    ) 

    return project,search_query