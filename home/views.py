from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cria-template')
    else:
        # Se o usuário não estiver logado ele rotorna uma instancia do form vazio
        form = AuthenticationForm()
    return render(request, "index.html", {'form': form})
