from django.contrib import admin
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from .models import User

# Register your models here.
class UserAdmin(AuthUserAdmin):
    add_form = MyUserCreationForm
    update_form_class = UserChangeForm
