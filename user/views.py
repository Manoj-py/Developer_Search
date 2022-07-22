from django.shortcuts import render,redirect
from .models import Profile,User
from projects.models import Tag
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .helper import searchProfile

from .forms import CustomUserCreationForm,ProfileForm,SkillForm
from django.contrib.auth.decorators import login_required


def loginUser(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request,"User Doesnot Exists")

        user = authenticate(request, username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
           messages.error(request,"Username or password incorrect")

    context = {"page":page}    

    return render(request,'users/login_register.html',context)

def logoutUser(request):
    logout(request)
    messages.info(request,"User LoggedOut Succesfully")
    return render(request,'users/login_register.html')


def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request,"Account Created Succesfully!!")

            login(request,user)
            return redirect('account')
        else:
            messages.error(request, "An Error occurred During User Creation")


    context = {'page':page,"form":form}
    return render(request,"users/login_register.html",context)



def profiles(request):
    profiles,search_query = searchProfile(request)
        
    tags = Tag.objects.all()
    context = {'profiles':profiles,
    'tags':tags,'search_query':search_query}
    return render(request, "users/profiles.html",context)

def userprofiles(request,pk):
    profile = Profile.objects.get(id=pk)
    topskills = profile.skill_set.exclude(descripition__exact ="")
    other_skills = profile.skill_set.filter(descripition ="")
    context = {'profile':profile,"topskills":topskills,"other_skills":other_skills}
    return render(request, 'users/users-profile.html',context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    
    context = {'profile':profile,'skills':skills,'projects': projects}
    
    return render(request, 'users/account.html',context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {"form":form}

    return render(request, "users/editaccount.html",context)

@login_required(login_url='login')
def createSkill(request):
    profile = request.user.profile
    form = SkillForm()
    
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(request,"Skill Created Sucessfully")

            return redirect('account')

    context = {'form':form}
    return render(request,"users/skill_form.html",context)

@login_required(login_url='login')
def updateSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    
    if request.method == "POST":
        form = SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,"Skill Updated Sucessfully")

            return redirect('account')

    context = {'form':form}
    return render(request,"users/skill_form.html",context)

@login_required(login_url='login')
def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.success(request,"Skill Deleted Sucessfully")
        return redirect('account')

    context = {'object':skill}
    return render(request, 'delete_template.html',context)
