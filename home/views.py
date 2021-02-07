from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import AuthenticationForm
from .forms import MeuAutoForm


# Create your views here.

def home(request):
    if request.method == 'POST':
        form = MeuAutoForm(data=request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    return redirect('cria-template')
    else:
        # Se o usuário não estiver logado ele rotorna uma instancia do form vazio
        form = MeuAutoForm()
    return render(request, "index.html", {'form': form})
