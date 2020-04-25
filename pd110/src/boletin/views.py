from django.shortcuts import render

from .forms import RegForm
from .models import Registrado

# Create your views here.
def inicio(request):
	form = RegForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		campo_email =  form_data.get("email")
		campo_nombre = form_data.get("nombre")
		objeto = Registrado.objects.create(email=campo_email, nombre=campo_nombre)

		#obj = Registrado
		#obj.email = campo_email
		#obj.save()

	context = {
		"el_form": form,
	}
	return render(request, "inicio.html", context)