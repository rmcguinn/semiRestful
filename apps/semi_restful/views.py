# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import *
from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request, "index.html", { "users": User.objects.all()})

def new_user(request):
    return render(request, "new_user.html")

def create(request):
    User.objects.create(name=request.POST["name"], email=request.POST["email"])
    return redirect("/")

def show(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, "show.html", context)

def edit(request, user_id):
    context = {
        "user": User.objects.get(id=user_id)
    }
    return render(request, "update.html", context)

def update(request, user_id):
    user_to_update = User.objects.get(id=user_id)
    user_to_update.name = request.POST["name"]
    user_to_update.email = request.POST["email"]
    user_to_update.save()
    return redirect("/")

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/")