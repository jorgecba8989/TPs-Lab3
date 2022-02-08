from django.http import HttpResponse

from django.template import Template, Context

def saludo(request):
    documento="<html><body><div class='container'><h2>hola mundoooo</h2></div></body></html>"
    return HttpResponse(documento)


def contenidoHTML(request):
    contenido = open("E:/Documentos/Lab3/TPs-Lab3/ProyectoFinal/JyRCards/JyRCards/templates/index.html")
    template = Template (contenido.read())
    contenido.close()
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)