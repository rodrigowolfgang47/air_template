from django.shortcuts import render, get_object_or_404, redirect
from criador_de_template.models import Cliente, Usuario
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def meus_templates(request):

    #busca aqui
    termo_buscado = request.GET.get('pesquisa', None)
    
    if termo_buscado:

        usuario = Usuario.objects.get(username=request.user)

        lista_de_clientes = usuario.cliente_set.filter(cliente__icontains=termo_buscado).order_by('-criacao')

        paginador = Paginator(lista_de_clientes, 6)
        pagina = request.GET.get('page')

        clientes = paginador.get_page(pagina)
        
    else:
        usuario = Usuario.objects.get(username=request.user)

        lista_de_clientes = usuario.cliente_set.all().order_by('-criacao')

        paginador = Paginator(lista_de_clientes, 6)
        pagina = request.GET.get('page')

        clientes = paginador.get_page(pagina)

    return render(request, 'meus_templates.html', {'clientes': clientes, 'pesquisa': termo_buscado})

def deletar_cliente(request, cliente):
    cliente_delete = get_object_or_404(Cliente, pk=cliente)

    if request.method == 'POST':
        cliente_delete.delete()
        return redirect('meus_templates')
    else:
        return render(request, 'cliente_delete.html', {'cliente': cliente_delete})

def meu_cliente(request, cliente):
    
    cliente = get_object_or_404(Cliente, pk=cliente)
    produtos = cliente.produto_set.all()

    return render(request, 'template_final.html', {'produtos': produtos})