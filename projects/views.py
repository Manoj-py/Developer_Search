from django.shortcuts import redirect, render
from .models import Project, Tag
from django.shortcuts import render
from .forms import ProjectForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .helper import searchProjects
from django.contrib.auth.decorators import login_required


def projects(request):
    project,search_query = searchProjects(request)  

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(project,results)

    try:
        project = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        project = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        project = paginator.page(page)


    context = {'projects': project, "search_query":search_query,'paginator':paginator}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projectobj = Project.objects.get(id=pk)
    context = {'project':projectobj}
    return render(request,'projects/single-project.html',context)


@login_required(login_url='login')
def createproject(request):
    profile = request.user.profile
    projectform = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid:
            project = form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('account')
    context = {'form':projectform}
    return render(request, 'projects/createproject.html', context)

@login_required(login_url='login')
def updateproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    projectform = ProjectForm(instance=project)
    if request.method == "POST":
        form = ProjectForm(request.POST,request.FILES, instance=project)
        if form.is_valid:
            form.save()
            return redirect('account')
    context = {'form':projectform}
    return render(request, 'projects/createproject.html', context)



@login_required(login_url='login')
def deleteproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)

    if request.method == "POST":
        project.delete()

        return redirect('account')

    context = {'object':project}
    
    return render(request, 'delete_template.html', context)








 