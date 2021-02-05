from django.shortcuts import render
from criador_de_template.models import Cliente
from django.core.paginator import Paginator

# Create your views here.


def meus_templates(request):
    lista_de_clientes = Cliente.objects.all().order_by('-criacao')

    paginador = Paginator(lista_de_clientes, 3)
    pagina = request.GET.get('page')

    clientes = paginador.get_page(pagina)

    return render(request, 'meus_templates.html', {'clientes': clientes})