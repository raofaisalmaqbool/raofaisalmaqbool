from django.shortcuts import render

from myapp.forms import Add_Student

# Create your views here.

def add_show(request):
    if request.method == 'POST':
        data = Add_Student(request.POST)
    else:
        data = Add_Student()
    return render(request, "addandshow.html", {'context':data})

def base(request):
    return render(request, "base.html")
