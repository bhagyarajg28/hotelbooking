from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from app1.models import Room, Book
import datetime


# Create your views here.
def home(request):
    return render(request, 'base1.html')


def registration(request, **kwargs):
    if request.method == "POST":
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
            return redirect(loginn)
        else:
            return render(request, 'register.html', {'f': f})
    else:
        f = UserCreationForm()
        return render(request, 'register.html', {'f': f})


def loginn(request):
    if request.method == "POST":
        t1 = request.POST['t1']
        t2 = request.POST['t2']
        user = authenticate(username=t1, password=t2)
        if user is not None:
            login(request, user)
            return redirect(room)
        return redirect(registration)
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return render(request, 'base1.html')


@login_required
def room(request):
    if request.method == 'POST':
        t2 = request.POST['t1']
        print(t2)
        print(type(t2))

        t3 = datetime.datetime.strptime(t2, '%Y-%m-%d')
        print(t3)
        print(type(t3))
        time = datetime.datetime.now()
        print(time)
        list1 = Room.objects.filter(Date__exact=t3)
        return render(request, 'base.html', {'list1': list1, 'time': time})
    else:
        return render(request, 'base.html')


@login_required
def booking(request, *args, **kwargs):
    id = kwargs.pop("id")
    print(id)
    l = Room.objects.get(pk=id)
    l.availability = False
    l.save()
    b = Book.objects.create(user=request.user, room_no=l, time=datetime.datetime.now())
    if b.room_no.Date == l.Date:
        b.save()
    return render(request, 'booking.html', {'b': b})
