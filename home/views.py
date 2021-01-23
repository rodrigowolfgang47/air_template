from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #o usuário está logado
            return redirect('https://www.youtube.com/')
    else:
        # Se o usuário não estiver logado ele rotorna uma instancia do form vazio
        form = AuthenticationForm()
    return render(request, "index.html", {'form': form})
