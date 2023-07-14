"""
URL configuration for Entrega_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include, path
from .views import LandingPage, IndexPage, ContactoPage,NosotrosPage , PromocionesPage, ServiciosPage



urlpatterns = [
    path('admin/', admin.site.urls),
    #path('' ,LandingPage.as_view() , name="landing_page"),
    path('' ,IndexPage.as_view() , name ="index"),
    path('contacto' ,ContactoPage.as_view() , name ="contacto"),
    path('nosotros' ,NosotrosPage.as_view() , name ="nosotros"),
    path('promociones' ,PromocionesPage.as_view() , name ="promociones"),
    path('servicios' ,ServiciosPage.as_view() , name ="servicios"),
    
]
