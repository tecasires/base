# Necesitaremos importar el objeto 'HttpResponse' para poder trabajar con él.
from django.http import HttpResponse

# Importamos el render que vamos a utilizar.
from django.shortcuts import render


# Definimos nuestra primera vista llamada my_view en la que le decimos que realizarnos un 'request' devuelva 'My view'
def my_view(request):
    return HttpResponse('Esta es mi vista')

# from django.template import Template, Context
def my_template(request):
	return render(request, "my_template.html", context = {})
