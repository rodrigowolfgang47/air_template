from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .form import Cadastro
from .tokens import account_activation_token

# from django.contrib.auth import login, authenticate
# fom django.contrib.auth.forms import UserCreationForm




# Create your views here.


# view responsável por cadastrar e enviar token de ativação
def cadastro(request):
    form = Cadastro()

    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.first_name = request.POST.get('first_name')
            user.profile.last_name = request.POST.get('last_name')
            user.profile.email = request.POST.get('email')
            # Se o usuário não ativar o e-mail não pode logar
            user.is_activate = False
            user.save()
            current_site = get_current_site(request)
            subject = f'Ative sua conta clicando no link'

            mensagem = render_to_string('requisicao_de_ativacao.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, mensagem)
            return redirect('ativador_enviado')

            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return redirect('home')
            # outra forna de redirecionar o usuário ----> return HttpResponseRedirect('http://127.0.0.1:8000/')

    return render(request, 'cadastro.html', {'form': form})

# view exibe mensagem após o cafastro com sucesso e confirmação de e-mail
def activation_sent_view(request):
    return render(request, 'activation_sent_view.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.signup_confirmation = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'activation_invalid.html')