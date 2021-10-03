from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from BloodBank.models import Bloody


# def home(request):
#     return render(request, 'home.html')

def home(request):
    request.GET()
    return render(request, 'login.html')


def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            data = Bloody.objects.all()
            return render(request, 'display.html', {'data': data})
        else:
            messages.error(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def register(request):

    if request.method == 'POST':
        blood1 = Bloody()
        # blood1.firstname = request.POST['firstname']
        # blood1.lastname = request.POST['lastname']
        blood1.username = request.POST['username']
        # blood1.email = request.POST['email']
        # blood1.blood = request.POST['blood']
        # blood1.contact = request.POST['contact']
        blood1.password1 = request.POST['password1']
        blood1.password2 = request.POST['password2']
        if blood1.password1 == blood1.password2:
            if User.objects.filter(username=blood1.username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=blood1.email).exists():
                messages.info(request, 'email taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=blood1.username, password=blood1.password1)
                user.save()
                return render(request, 'login.html')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')
    else:
        return render(request, 'register.html')


def add_donor(request):
    return render(request, 'add_donor.html')


def display(request):
    blood2 = Bloody()
    blood2.firstname = request.POST['firstname']
    blood2.lastname = request.POST['lastname']
    blood2.email = request.POST['email']
    blood2.blood = request.POST['blood']
    blood2.contact = request.POST['contact']
    blood2.save()
    data = Bloody.objects.all()
    return render(request, 'display.html', {'data': data})


def logout(request):
    auth.logout(request)
    return redirect('login')



