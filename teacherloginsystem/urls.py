from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('teacherregistration', views.register, name='teacherregistration'),
    path('afterRegister', views.afterRegister, name='afterRegister'),
    path('teacherLogin', views.teacherLogin, name='teacherLogin'),
    path('afterTeacherLogin', views.afterTeacherLogin, name='afterTeacherLogin'),
    path('addQuestionForm', views.addQuestionForm, name='addQuestionForm'),
    path('afterAdd', views.afterAdd, name='afterAdd'),
    path('viewScore', views.viewScore, name='viewScore'),
]