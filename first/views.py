from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import Students, Scores

# Create your views here.
@csrf_exempt
def index(request):
    print('하람', request.method)
    print('하람', request.GET)
    print('하람', request.headers)
    
    return render(request, 'first/index.html')

def students(request):
    students = Students.objects.all() # select * from students 와 같음
    return render(request, 'first/students.html', {
        'text' : '안녕하세요!',
        'students': students
    })

def students_detail(request, id):
    students = Students.objects.filter(pk=id) # select * from students 와 같음
    print('한 번 찍어보기',id)
    return render(request, 'first/students.html', {
        'text' : '안녕하세요!',
        'students': students
    })

def scores(request):   
    scores = Scores.objects.all() # select * from scores 와 같음
    return render(request, 'first/scores.html', {
        'scores': scores
    })