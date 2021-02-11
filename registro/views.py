from django.contrib.auth import login
from criador_de_template.models import Usuario
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .form import Cadastro
from .tokens import account_activation_token
from django.core.mail import send_mail


# from django.contrib.auth import login, authenticate
# fom django.contrib.auth.forms import UserCreationForm


# Create your views here.


# view responsável por cadastrar e enviar token de ativação
def cadastro(request):
    if request.method == 'POST':
        form = Cadastro(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            # testar se o usuario é cadastrado se não voltar com o cod abaixo
            user.save()

            #user.refresh_from_db()

            user.profile.first_name = form.cleaned_data.get('first_name')
            user.profile.last_name = form.cleaned_data.get('last_name')
            user.profile.email = form.cleaned_data.get('email')

            # Se o usuário não ativar o e-mail não pode logar
            current_site = get_current_site(request)
            subject = 'Ative sua conta clicando no link'

            mensagem = render_to_string('requisicao_de_ativacao.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = user.profile.email
            send_mail(subject, mensagem, 'rodrigocosta47@outlook.com', [to_email],
                      fail_silently=False)

            return redirect('ativador_enviado')

            # username = request.POST.get('username')
            # password = request.POST.get('password')
            # user = authenticate(username=username, password=password)
            # login(request, user)
            # return redirect('home')
            # outra forna de redirecionar o usuário ----> return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = Cadastro()
    return render(request, 'cadastro.html', {'form': form})


# view exibe mensagem após o cafastro com sucesso e confirmação de e-mail
def activation_sent_view(request):
    return render(request, 'activation_sent_view.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Usuario.objects.get(pk=uid)
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
