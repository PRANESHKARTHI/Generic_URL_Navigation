from django.shortcuts import render

# Create your views here.
def marks(request):
    return render(request,"marks.html")

def passing(request):
    return render(request,"passing.html")

def failing(request):
    return render(request,"failing.html")