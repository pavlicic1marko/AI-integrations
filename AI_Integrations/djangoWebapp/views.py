from django.shortcuts import render


def home(reqeuest):
    return render(reqeuest, 'authenticate/home.html', {})
