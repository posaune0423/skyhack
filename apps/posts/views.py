from django.shortcuts import render

# Create your views here.
def top(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'posts/index.html')

def show(request):
    return render(request, 'posts/show.html')