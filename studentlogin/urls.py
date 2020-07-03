from django.urls import path, include
from . import views

urlpatterns = [
    path('studentLogin', views.studentLogin, name='studentLogin'),
    path('afterStudentLogin', views.afterStudentLogin, name='afterStudentLogin'),
    path('afterQuiz', views.afterQuiz, name='afterQuiz'),
]