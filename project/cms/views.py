from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Content
from django.views.decorators.csrf import csrf_exempt

formulario = """
No existe valor en la base de datos para esta llave.
<p>Introdúcela:
<p>
<form action="" method="POST">
    Valor: <input type="text" name="valor">
    <br/><input type="submit" value="Submit">
</form>
"""


@csrf_exempt
def get_content(request, key):

    if request.method == "POST":
        value = request.POST['valor']

        try:
            # if the shortened url have been stored in a previous POST, we
            # remove it and add the new content.
            content = Content.objects.get(key=key)
            content.delete()
        except Content.DoesNotExist:
            pass

        content = Content(key=key, value=value)
        content.save()
        content.save()

    elif request.method == "PUT":
        value = request.body.decode('utf-8')
        try:
            content = Content.objects.get(key=key)
            content.delete()
        except Content.DoesNotExist:
            pass

        content = Content(key=key, value=value)
        content.save()

    try:
        response = Content.objects.get(key=key).value
    except Content.DoesNotExist:
        response = 'No existe contenido para la clave ' + value + '\n' + formulario
    except Content.MultipleObjectsReturned:
        respuesta = Content.objects.filter(key=key).last().valor

    return HttpResponse(response)
