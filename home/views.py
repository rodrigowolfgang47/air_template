from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

def home(req):
    if req.method == 'POST':
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            form.save()
            #o usuário está logado
            return redirect('novo_template')
    else:
        # Se o usuário não estiver logado ele rotorna uma instancia do form vazio
        form = AuthenticationForm()
    return render(req, "index.html", {'form': form})
