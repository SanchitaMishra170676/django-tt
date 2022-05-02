from django.shortcuts import render, redirect

def index(request):
    if request.method =='POST':
        pass
    return render(request,'index.html')