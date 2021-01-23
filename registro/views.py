from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def cadastro(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        #outra forna de redirecionar o usuário ----> return HttpResponseRedirect('http://127.0.0.1:8000/')
        return redirect('home')

    return render(request, 'cadastro.html', {'form':form})
