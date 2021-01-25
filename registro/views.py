from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
# fom django.contrib.auth.forms import UserCreationForm
from .form import Cadastro


# Create your views here.

def cadastro(request):
    form = Cadastro(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = request.POST.get('first_name')
        user.profile.last_name = request.POST.get('last_name')
        user.profile.email = request.POST.get('email')
        user.save()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
        # outra forna de redirecionar o usuário ----> return HttpResponseRedirect('http://127.0.0.1:8000/')

    return render(request, 'cadastro.html', {'form': form})
