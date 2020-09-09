from django.shortcuts import render
from .models import Favourite, Todo, TodoGroup

# Create your views here.
def index(request):   
    return render(request, 'second/index.html')

def layout(request):   
    return render(request, 'second/layout.html')

def favourites(request):   
    favourite = Favourite.objects.all() # select * from favourite 와 같음
    return render(request, 'second/favourite.html', {
        'favourites': favourite
    })

def favourites_detail(request, id):   
    fav_detail = Favourite.objects.get(seq=id)
    # print('뽑은 값을 알려주ㅓ!',fav_detail.values())
    print(fav_detail)
    return render(request, 'second/favourite_detail.html', {
        'favourite': fav_detail
    })

def todo(request):
    data = Todo.objects
    pending = data.filter(status='pending')
    inprogress = data.filter(status='inprogress')
    end = data.filter(status='end')

    return render(request, 'second/todo.html', {
        'pendings': pending,
        'inprogress' : inprogress,
        'ends' : end
    })

def todo_detail(request, id):
    data = Todo.objects.get(pk=id)

    return render(request, 'second/todo_detail.html', {
        'todo': data
    })

# def todos(request):   
#     todo = Todo.objects.all() # select * from todo 와 같음
#     text = request.GET

#     if ('group' in text) & ('end_date' in text):
#         group = text['group']
#         end_date = text['end_date']
#         todo = Todo.objects.filter(group__name=group).filter(end_date__gte=end_date)
#     elif 'group' in text:
#         group = text['group']
#         todo = Todo.objects.filter(group__name=group)   
#     elif 'end_date' in text:
#         end_date = text['end_date']
#         todo = Todo.objects.filter(end_date__gte=end_date)

#     return render(request, 'second/todo_td.html', {
#         'todos': todo
#     })




# def todo(request):
#     data = Todo.objects
#     if 'group' in request.GET:
#         data = data.filter(group__name=request.GET['group'])
#     if 'end_date' in request.GET:
#         data = data.filter(end_date__gte=request.GET['end_date'])
#     return render(request, "second/todo.html",
#         {'datas':data.all()}
#     )
