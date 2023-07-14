from django.views.generic import TemplateView



class LandingPage(TemplateView):
    template_name = "landing_page.html"

    extra_context ={
        "titulo_pagina" : "LANDING PAGE"
    }

class IndexPage(TemplateView):
    template_name = "index.html"

class ContactoPage(TemplateView):
    template_name = "pages/contacto.html"

class NosotrosPage(TemplateView):
    template_name = "pages/nosotros.html"

class PromocionesPage(TemplateView):
    template_name = "pages/promociones.html"

class ServiciosPage(TemplateView):
    template_name = "pages/servicios.html"



    
