"""air_template URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home import url as home_urls
from registro import url as cadastro_urls
from criador_de_template import url as cria_templates_urls
from administracao_clientes import url as meus_template_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(home_urls), name='home'),
    path('', include(cadastro_urls), name='cadastro'),
    path('', include(cria_templates_urls), name='cria-template'),
    path('', include(meus_template_urls), name='meus_templates')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
