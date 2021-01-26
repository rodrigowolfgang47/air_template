from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
@login_required()
def crie_seu_template(request):
    return render(request, 'crie_seu_template.html')

def sair(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
