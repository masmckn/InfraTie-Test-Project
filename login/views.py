from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.http import require_POST
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', '/home/')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, "login/index.html")

@require_POST
def logout_view(request):
    logout(request)
    return redirect('/login/')
