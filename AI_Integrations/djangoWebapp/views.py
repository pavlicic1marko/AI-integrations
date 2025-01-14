from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .ChatGpt.client import ask_chat_gpt
from .forms import SignUpForm, EditProfileForm
from .models import ChatGptPrompts
from .ollamaClient.ollama_client import ollama_chat

chat_history = []


def home(reqeuest):
    return render(reqeuest, 'authenticate/home.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out'))
    return redirect('home')


def login_user(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ('You Have been logged in!'))
            return redirect('home')
        else:
            messages.error(request, ('The user with credentials does not exist'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('You Have Registered successfully'))
            return redirect('home')
    else:
        form = SignUpForm()

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)


def chat_gpt_prompt_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question = request.POST.get('question')
            model = request.POST.get('category')

            answer = ask_chat_gpt(question, model)

            chat_gpt_prompt = ChatGptPrompts(question=question, answer=answer, user=request.user, aiModel=model)
            chat_gpt_prompt.save()  # Save to the database

            chat_history.append({'question': question, 'answer': answer})
            return render(request, 'authenticate/prompt.html', {'questions': chat_history})
        else:
            return render(request, 'authenticate/prompt.html')
    else:
        return render(request, 'authenticate/home.html')


def ollama_prompt_page(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            question = request.POST["question"]
            answer = ollama_chat(question)

            chat_gpt_prompt = ChatGptPrompts(question=question, answer=answer, user=request.user, aiModel='ollama 3.1:1b')
            chat_gpt_prompt.save()  # Save to the database

            chat_history_llama = [{'question': question, 'answer': answer}]

            return render(request, 'authenticate/ollama-prompt.html', {'questions': chat_history_llama})
        else:
            return render(request, 'authenticate/ollama-prompt.html')

    else:
        return render(request, 'authenticate/home.html')


def user_chat_history(request):
    all_items = ChatGptPrompts.objects.filter(user=request.user, )

    return render(request, 'authenticate/chat-history.html',{'all_items': all_items})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('You Have Edited Your Profile Information'))
            return redirect('home')
    else:
        form = EditProfileForm(instance=request.user)

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ('you have successfully changed your password'))
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)

    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)