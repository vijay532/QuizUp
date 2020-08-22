from django.shortcuts import render
from .models import Question,Choice
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse 
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

def index(request):
    question=Question.objects.all()
    #choice_arr=Choice.objects.all()
    #context={'latest_question':question_ele}
    #contextc={'latest_choice':choice_arr}
    context={'latest_question':question}
    return render(request,'quizTemplate/index.html',context)
 
#Show specific question and choices 
  
def detail(request, question_id): 
    try: 
        question = Question.objects.get(pk = question_id) 
    except Question.DoesNotExist: 
        raise Http404("Question does not exist") 
    return render(request, 'quizTemplate/detail.html', {'question': question}) 

# Get question and display results

def results(request, question_id): 
    question = get_object_or_404(Question, pk = question_id) 
    return render(request, 'quizTemplate/results.html', {'question': question}) 


# Vote for a question choice 
  
  
def vote(request, question_id): 
    # print(request.POST['choice']) 
    question = get_object_or_404(Question, pk = question_id) 
    try: 
        selected_choice = question.choice_set.get(pk = request.POST['choice']) 
    except (KeyError, Choice.DoesNotExist): 
        # Redisplay the question voting form. 
        return render(request, 'quizTemplate/detail.html', { 
            'question': question, 
            'error_message': "You didn't select a choice.", 
        }) 
    else: 
        selected_choice.votes += 1
        selected_choice.save() 
        # Always return an HttpResponseRedirect after successfully dealing 
        # with POST data. This prevents data from being posted twice if a 
        # user hits the Back button. 
        return HttpResponseRedirect(reverse('QuizApp:results', args =(question.id, ))) 