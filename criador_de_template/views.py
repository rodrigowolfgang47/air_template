from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
import mimetypes
import pandas as pd


# Create your views here.
@login_required()
def crie_seu_template(request):
    return render(request, 'crie_seu_template.html')


def sair(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')


def download_file(request):
    file_path = "criador_de_template/staticfiles/excel/base_air_template_layout.xlsx"
    file_name = 'base_air_template_layout.xlsx'

    file = pd.read_excel(file_path)
    mime_type, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_type)
    response['Content-Disposition'] = "attachment; file_name=%s" % file_name
    return response
