from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth import views as auth_views
