from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Customer


def index_page(request):
    data = Customer.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


def edit_page(request):
    return render(request, "edit.html")


def login_page(request):
    return render(request, "login.html")


def signup_page(request):
    return render(request, "signup.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        room = request.POST.get('room')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        date = request.POST.get('date')

        query = Customer(name=name, email=email, room=room, gender=gender, address=address, date=date)
        query.save()
        return redirect("/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Customer.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        room = request.POST.get('room')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        date = request.POST.get('date')

        update_info = Customer.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.room = room
        update_info.gender = gender
        update_info.address = address
        update_info.date = date

        update_info.save()
        return redirect("/")

    d = Customer.objects.get(id=id)
    context = {"d": d}
    return render(request, "edit.html", context)

