from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Inspection

# Create your views here.
@login_required
def home(request):
    inspect_list = Inspection.objects.all()
    context = {'username': request.user.username, 'inspect_list': inspect_list}
    return render(request, "home/home.html", context)