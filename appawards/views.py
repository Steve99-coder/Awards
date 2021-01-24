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
