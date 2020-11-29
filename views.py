from django.shortcuts import render, HttpResponseRedirect
from App_Login.forms import CreateNewUser
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from App_Login.models import UserProfile


def sign_up(request):
    form = CreateNewUser()
    registered = False
    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            return HttpResponseRedirect(reverse('App_Login:login'))

    return render(request, 'App_Login/signup.html',
                  context={'title': 'sign up . Instagram', 'form': form})


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                pass

    return render(request, 'App_Login/login.html', context={'title': 'login', 'form': form})


# afa
# afa@gmail.com
# afatumikoi
