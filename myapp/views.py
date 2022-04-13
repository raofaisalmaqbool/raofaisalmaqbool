from django.shortcuts import render
from .models import *
from myapp.forms import Add_Student

# Create your views here.


def add_show(request):
    # print("in add_show mathod")
    if request.method == "POST":
        # print("in post mathod with post")
        data = Add_Student(request.POST)
        # print(data)
        if data.is_valid():
            # print("is valid data")
            data.save()
    else:
        print("in add_show mathod with get")
        data = Add_Student()
    return render(request, "addandshow.html", {'context': data})


def base(request):
    return render(request, "base.html")
