from django.shortcuts import render,redirect
from .models import Profile,Project,Comment
import datetime as dt

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    current_user = request.user
    user_profile= Profile.objects.filter(user=current_user.id).first()
    comment= Comment.objects.filter(user=current_user.id).first()
    projects = Project.objects.all()
    average=0

    for project in projects:
        average=(project.design + project.usability + project.content)/3
        rating = round(average,2)
    return render(request, 'users/index.html', {'user_profile':user_profile, 'projects':projects,'comment':comment})


@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
  
    if request.method == 'POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()

        return redirect ("welcome")

    else:
        form = NewProjectForm()

    return render(request, 'users/new_project.html', {"form": form})

def search_results(request):

    if 'title' in request.GET and request.GET["title"]:
        search_term = request.GET.get("title")
        searched_projects = Project.search_project(search_term)
        current_user=request.user
        message = f"{search_term}"
        return render(request, 'users/search.html',{"message":message,"titles": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'users/search.html',{"message":message})


