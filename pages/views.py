from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')


def service(request):
    return render(request, 'pages/service.html')

def error_404_view(request, exception):
    return render(request,'pages/exception/error_404.html')

def error_500_view(request):
    return render(request, 'pages/exception/error_500.html')