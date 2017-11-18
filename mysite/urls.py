"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin


# liste de regex qui determine les pages à sevir en fonction de l'url
# En Python, les expressions régulière commencent toujours par r au début de la chaîne de caractères. 
# Cela permet d'indiquer à Python que ce qui va suivre inclut des caractères qu'il ne doit pas interpréter 
# en tant que code Python mais en tant qu'expression régulière.


urlpatterns = [
    url(r'^admin/', admin.site.urls), # "celles qui commencent pas admin/"
    url(r'', include('blog.urls')),
]
