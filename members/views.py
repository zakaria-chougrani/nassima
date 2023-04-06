from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegistrationForm, AccountAuthenticationForm
from .models import MyUser


def login_view(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect("dashboard")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    return render(request, 'authenticate/login.html', context)


# def registration_view(request):
#     context = {}
#     if request.POST:
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             context['registration_form'] = form
#     else:
#         form = RegistrationForm()
#         context['registration_form'] = form
#     return render(request, "authenticate/signup.html", context)


def logout_view(request):
    logout(request)
    messages.success(request, "vous étiez déconnecté!")
    return redirect('login')

#
# @login_required(login_url='login')
# def users_list(request):
#     context = {}
#
#     users = MyUser.objects.all()
#     context["users"] = users
#
#     return render(request, 'list_users.html', context)
#
#
# @login_required(login_url='login')
# def profile_view(request):
#     context = {}
#     current_user = request.user
#     context["current_user"] = current_user
#     return render(request, "profile.html", context)
