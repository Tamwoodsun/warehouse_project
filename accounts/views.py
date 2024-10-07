from django.shortcuts import render, get_object_or_404, redirect
#from user.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from transfer.models import Transfer
from django.contrib import auth

# Create your views here.

# return to dashboard, show his information and record
@login_required
def dashboard(request):
    transfer_rec = Transfer.objects.filter(user=request.user)
    context = {'transfer': transfer_rec}
    return render(request, 'accounts/dashboard.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return redirect("/exception/error_404.html")
    else:
        return render(request, 'accounts/login.html')

@login_required
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect("index")

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email,password=password)
        user.save()
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')