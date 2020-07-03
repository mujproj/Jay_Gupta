from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def home(request):

    return render(request, 'home.html')

def register(request):

    rForm = registerForm()
    return render(request, 'teacherloginsystem/register.html', {'rForm': rForm})

def afterRegister(request):

    if request.method == "POST":

        rForm = registerForm(request.POST)
        if rForm.is_valid():

            if(request.POST["password"] != request.POST["confirm_password"]):

                return render(request, 'teacherloginsystem/register.html', {'rForm': rForm, 'error': 'Passwords Donot Match'})

            if(len(request.POST["username"]) < 3):

                return render(request, 'teacherloginsystem/register.html', {'rForm': rForm, 'error': 'Username should be greater than 3 characters'})

            if len(request.POST["password"]) < 6:

                return render(request, 'teacherloginsystem/register.html', {'rForm': rForm, 'error': 'Password should be atleast 6 characters'})

            else:

                user = teacherRegister(username=rForm.cleaned_data["username"], password=rForm.cleaned_data["password"])
                user.save()
                return redirect('teacherLogin')

        else:

            return render(request, 'teacherloginsystem/register.html', {'rForm': rForm, 'error': rForm.errors})

def teacherLogin(request):

    lForm = teacherLoginForm()
    return render(request, 'teacherloginsystem/login.html', {'lForm': lForm})

def afterTeacherLogin(request):

    if request.method == "POST":

        lForm = teacherLoginForm(request.POST)
        if lForm.is_valid():

            if request.POST["username"] not in teacherRegister.objects.values_list('username', flat=True):

                return render(request, 'teacherloginsystem/login.html', {'lForm': lForm, 'error': 'Username does not exist'})

            else:

                user = teacherRegister.objects.filter().values('username', 'password')
                for u in user:

                    if request.POST["username"] in u['username']:

                        if request.POST["password"] not in u['password']:

                            return render(request, 'teacherloginsystem/login.html', {'lForm': lForm, 'error': 'Username Password Mismatch'})

                request.session["username"] = request.POST["username"]
                return redirect('addQuestionForm')

        else:

            return render(request, 'teacherloginsystem/login.html', {'error': lForm.errors})

def addQuestionForm(request):

    return render(request, 'teacherloginsystem/addQuestionForm.html')

def afterAdd(request):

    if request.method == "POST":

        user = questions(
            username=request.session["username"],
            question1=request.POST["question1"], answer1=request.POST["answer1"], options1=request.POST["options1"],
            question2=request.POST["question2"], answer2=request.POST["answer2"], options2=request.POST["options2"],
            question3=request.POST["question3"], answer3=request.POST["answer3"], options3=request.POST["options3"],
            question4=request.POST["question4"], answer4=request.POST["answer4"], options4=request.POST["options4"],
            question5=request.POST["question5"], answer5=request.POST["answer5"], options5=request.POST["options5"],
            question6=request.POST["question6"], answer6=request.POST["answer6"], options6=request.POST["options6"],
            question7=request.POST["question7"], answer7=request.POST["answer7"], options7=request.POST["options7"],
            question8=request.POST["question8"], answer8=request.POST["answer8"], options8=request.POST["options8"],
            question9=request.POST["question9"], answer9=request.POST["answer9"], options9=request.POST["options9"],
            question10=request.POST["question10"], answer10=request.POST["answer10"], options10=request.POST["options10"],
            studentsid=request.POST["student"],
            password_for_quiz=request.POST["password_for_quiz"]
        )
        user.save()
        return render(request, 'teacherloginsystem/addQuestionForm.html', {'message': 'Questions have been added'})

def viewScore(request):

    user = studentdata.objects.all().filter(username=request.session["username"]).values("username", "password", "regNumber", "score").order_by('password')
    print(user)
    # for u in user:

        # if request.session["username"] == u['username']:

        #     # return render(request, 'teacherloginsystem/viewScore.html', {'score': u['score'], 'studentNumber': u['regNumber'], 'password': u['password']})
        #     print(user[''])
        #     return render(request, 'teacherloginsystem/viewScore.html', {'score': user['score'], 'password': user['password'], 'studentNumber': user['regNumber']})
    return render(request, 'teacherloginsystem/viewScore.html', {'user': user})