# Necesitaremos importar el objeto 'HttpResponse' para poder trabajar con él.

from django.http import HttpResponse


	# Definimos nuestra primera vista llamada my_view en la que le decimos que realizarnos un 'request' devuelva 'My view'

def my_view(request):
    return HttpResponse('Esta es mi vista')
