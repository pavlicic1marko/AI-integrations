from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .ChatGpt.client import ask_chat_gpt
from .forms import SignUpForm
from .models import ChatGptPrompts

chat_history =[]

def home(reqeuest):
    return render(reqeuest, 'authenticate/home.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out...'))
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,('You Have been logged in!'))
            return redirect('home')
        else:
            messages.error(request,('Error'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html',{})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Registered...'))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'authenticate/register.html', context)

def chat_gpt_prompt_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question = request.POST["question"]
            answer = ask_chat_gpt(question)

            chat_gpt_prompt = ChatGptPrompts(question=question, answer=answer, user=request.user )
            chat_gpt_prompt.save()  # Save to the database



            chat_history.append({'question':question,'answer':answer})
            return render(request, 'authenticate/prompt.html', {'questions': chat_history})
        else:
            return render(request, 'authenticate/prompt.html')
    else:
        return render(request, 'authenticate/home.html')

