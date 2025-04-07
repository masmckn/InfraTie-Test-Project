from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Inspection, Condition

# Create your views here.
@login_required
def home(request):
    inspect_list = Inspection.objects.all()
    context = {'username': request.user.username, 'inspect_list': inspect_list}
    return render(request, "home/home.html", context)

@login_required
def conditions(request):
    if request.method == 'POST':
        inspect_id = request.POST.get('inspection_id')
        condition_list = Condition.objects.filter(Inspection_id=inspect_id)
        inspection = Inspection.objects.get(id=inspect_id)
        context = {'username': request.user.username, 'condition_list': condition_list, 'inspection': inspection}
        return render(request, "home/conditions.html", context)
    return redirect('/home/')