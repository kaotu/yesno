import random

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from answers.models import Answer

def answer_views(requests):
    answers = Answer.objects.all()
    answer = random.choice(answers)
    return render(requests, 'answer.html', context={'answer': answer})

def create_answer_views(requests):
    return render(requests, 'create_answer.html')

def add_create_answer_views(requests):
    result_text = requests.POST['text']
    result_image = requests.POST['image']
    create_answer = Answer.objects.create(text=result_text, image=result_image)
    return redirect('answer_views')

class CreateAnswerView(View):
    def get(self, requests, *args, **kwargs):
        return render(requests, 'create_answer.html')

    def post(self, requests, *args, **kwargs):
        result_text = requests.POST['text']
        result_image = requests.POST['image']
        create_answer = Answer.objects.create(text=result_text, image=result_image)
        return redirect('answer_views')
        
