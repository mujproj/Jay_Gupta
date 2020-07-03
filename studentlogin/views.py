from django.shortcuts import render
from .forms import *
from teacherloginsystem.models import *

a = ""
# Create your views here.
def studentLogin(request):

    lForm = studentLoginForm()
    return render(request, 'studentlogin/studentLoginForm.html', {'lForm': lForm})

def afterStudentLogin(request):

    global a
    if request.method == "POST":

        lForm = studentLoginForm(request.POST)
        if lForm.is_valid():

            if request.POST["password"] not in questions.objects.values_list('password_for_quiz', flat=True):

                return render(request, 'studentlogin/studentLoginForm.html', {'error': 'Invalid Password', 'lForm': lForm})

            else:
                a = request.POST["password"]
                user = questions.objects.filter().values(
                    'username', 'password_for_quiz', 'studentsid',
                    'question1', 'options1', 'answer1',
                    'question2', 'options2', 'answer2',
                    'question3', 'options3', 'answer3',
                    'question4', 'options4', 'answer4',
                    'question5', 'options5', 'answer5',
                    'question6', 'options6', 'answer6',
                    'question7', 'options7', 'answer7',
                    'question8', 'options8', 'answer8',
                    'question9', 'options9', 'answer9',
                    'question10', 'options10', 'answer10'
                )

                for u in user:

                    if request.POST["password"] == u["password_for_quiz"]:

                        if request.POST["username"] in u["studentsid"].split(", "):

                            for b in studentdata.objects.filter().values('regNumber', 'password'):

                                if request.POST["password"] == b['password']:

                                    if request.POST["username"] in b['regNumber'].split(", "):

                                        return render(request, 'studentlogin/studentLoginForm.html', {'lForm': lForm, 'error': 'Test has already been given'})

                            return render(request, 'studentlogin/quiz.html', {
                                'username': u['username'],
                                'q1': u['question1'], 'o1': u['options1'].split(", "),
                                'q2': u['question2'], 'o2': u['options2'].split(", "),
                                'q3': u['question3'], 'o3': u['options3'].split(", "),
                                'q4': u['question4'], 'o4': u['options4'].split(", "),
                                'q5': u['question5'], 'o5': u['options5'].split(", "),
                                'q6': u['question6'], 'o6': u['options6'].split(", "),
                                'q7': u['question7'], 'o7': u['options7'].split(", "),
                                'q8': u['question8'], 'o8': u['options8'].split(", "),
                                'q9': u['question9'], 'o9': u['options9'].split(", "),
                                'q10': u['question10'], 'o10': u['options10'].split(", "),
                                'p': a, 'user': request.POST["username"]
                            })

                        else:

                            return render(request, 'studentlogin/studentLoginForm.html', {'lForm': lForm, 'error': 'Username Does not exits'})

def afterQuiz(request):

    if request.method == "POST":

        count = 0
        incorrect = 0
        correct = 0
        user = questions.objects.filter().values(
            'username', 'password_for_quiz', 'studentsid',
            'question1', 'options1', 'answer1',
            'question2', 'options2', 'answer2',
            'question3', 'options3', 'answer3',
            'question4', 'options4', 'answer4',
            'question5', 'options5', 'answer5',
            'question6', 'options6', 'answer6',
            'question7', 'options7', 'answer7',
            'question8', 'options8', 'answer8',
            'question9', 'options9', 'answer9',
            'question10', 'options10', 'answer10'
        )

        for u in user:

            if request.POST["p"] == u['password_for_quiz']:

                if request.POST.get("options1", False) == u['answer1']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options1"])

                if request.POST.get("options2", False) == u['answer2']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options2"])

                if request.POST.get("options3", False) == u['answer3']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options3"])

                if request.POST.get("options4", False) == u['answer4']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options4"])

                if request.POST.get("options5", False) == u['answer5']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options5"])

                if request.POST.get("options6", False) == u['answer6']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options6"])

                if request.POST.get("options7", False) == u['answer7']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options7"])

                if request.POST.get("options8", False) == u['answer8']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options8"])

                if request.POST.get("options9", False) == u['answer9']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options9"])

                if request.POST.get("options10", False) == u['answer10']:

                    count = count + 1
                    correct = correct + 1

                else:

                    incorrect = incorrect + 1
                    # print(request.POST["options10"])

                a = studentdata(username=request.POST["username"], regNumber=request.POST["user"], password=request.POST["p"], score=count)
                a.save()
                return render(request, 'studentlogin/displayScore.html', {'score': count, 'correct': correct, 'incorrect': incorrect})