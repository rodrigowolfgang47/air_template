from django.shortcuts import render, get_object_or_404, redirect
from criador_de_template.models import Cliente
from django.core.paginator import Paginator

# Create your views here.


def meus_templates(request):
    lista_de_clientes = Cliente.objects.all().order_by('-criacao')

    paginador = Paginator(lista_de_clientes, 3)
    pagina = request.GET.get('page')

    clientes = paginador.get_page(pagina)

    return render(request, 'meus_templates.html', {'clientes': clientes})

def deletar_cliente(request, cliente):
    cliente_delete = get_object_or_404(Cliente, pk=cliente)

    if request.method == 'POST':
        cliente_delete.delete()
        return redirect('meus_templates')
    else:
        return render(request, 'cliente_delete.html', {'cliente': cliente_delete})