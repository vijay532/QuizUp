from django.shortcuts import render
from .models import Question,Choice
# Create your views here.

def ques(request):
    question_ele=Question.objects.all()
    #choice_arr=Choice.objects.all()
    #context={'latest_question':question_ele}
    #contextc={'latest_choice':choice_arr}
    return render(request,'index.html',{'latest_question':question_ele})