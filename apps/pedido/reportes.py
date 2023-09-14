import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders
from .models import Compras, Pedido  # Asegúrate de que este import esté al mismo nivel que los otros imports
from django.utils import timezone  # Agrega este import para utilizar timezone

def link_callback(uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        result = finders.find(uri)
        if result:
                if not isinstance(result, (list, tuple)):
                        result = [result]
                result = list(os.path.realpath(path) for path in result)
                path=result[0]
        else:
                sUrl = settings.STATIC_URL        # Typically /static/
                sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                mUrl = settings.MEDIA_URL         # Typically /media/
                mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                if uri.startswith(mUrl):
                        path = os.path.join(mRoot, uri.replace(mUrl, ""))
                elif uri.startswith(sUrl):
                        path = os.path.join(sRoot, uri.replace(sUrl, ""))
                else:
                        return uri

        # make sure that file exists
        if not os.path.isfile(path):
                raise Exception(
                        'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path

def reporte_compras(request):  # Corrige la indentación de esta función y cambia "reques" por "request"
    template_path = "pedido/compras_print_all.html"
    today = timezone.now()

    compras = Pedido.objects.all()  # Corrige el nombre de la clase de modelo y cambia "object" a "objects"
    context = {
        'obj': compras,
        'today': today,
        'request': request  # Corrige el nombre del parámetro
    }
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = 'inline; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def imprimir_compra(request, compra_id):
        template_path = "pedido/compras_print_one.html"
        today = timezone.now()
        
        enc=Pedido.objects.filter(id=compra_id).first()
        if enc:
                detalle=Compras.objects.filter(compra__id=compra_id)
        else:
                detalle={}
        context={
                'detalle': detalle,
                'encabezado': enc,
                'today' : today,
        }
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="report.pdf"'
        # find the template and render it.
        template = get_template(template_path)
        html = template.render(context)

        # create a pdf
        pisa_status = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)
        # if error then show some funny view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response
