from django.test import TestCase
from .models import Profile,Project,Comment
from django.contrib.auth.models import User
import datetime as dt

# Create your tests here.
class ProjectTestClass(TestCase):
    def setUp(self):

        self.new_user=User(id=1,username='Steve')
        self.new_profile=Profile(id=2,bio='Passion',profile_pic='pic.jpg',full_name='steveNderitu', user=self.new_user, email='stevenderitu99@gmail.com', phone_number='0708290960')
        self.new_project=Project(id=3,title='Philanthropists',image='pic.jpg', user=self.new_user, profile=self.new_profile, description='A perfect  project',vote=8,)

    def test_instance(self): 
        self.assertTrue(isinstance(self.new_profile,Profile))  
        self.assertTrue(isinstance(self.new_user,User))
        self.assertTrue(isinstance(self.new_project,Project))

    def test_save_project(self):
        self.new_project.save_project()
        projects=Project.objects.all()
        self.assertTrue(len(projects)>0)

    def tearDown(self):
        Project.objects.all().delete()

    def test_delete_project(self):
        self.new_project.delete_project()
        self.assertEqual(len(Project.objects.all()),0)
        
 