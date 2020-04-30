from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import  RegModelForm , ContactForm
from .models import Registrado

# Create your views here.
def inicio(request):
	titulo= "Bienvenido"
	if request.user.is_authenticated:
		titulo = "Bienvenido %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {
				"titulo" : titulo,
				"el_form" : form,
		}

	if form.is_valid():
		instance = form.save(commit=False)
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		if not instance.nombre:
			instance.nombre = "PERSONA"
		instance.save()

		context = {
			"titulo": "Gracias %s!" %(nombre)
		}

		if not nombre:
			context = {
				"titulo" : "Gracias %s" %(email)
			}

		print (instance)
		print (instance.timestamp)
		#form_data = form.cleaned_data
		#campo_email =  form_data.get("email")
		#campo_nombre = form_data.get("nombre")
		#objeto = Registrado.objects.create(email=campo_email, nombre=campo_nombre)

		#obj = Registrado
		#obj.email = campo_email
		#obj.save()

	if request.user.is_authenticated and request.user.is_staff:
		queryset = Registrado.objects.all().order_by("-timestamp")
		context = {
			"queryset": queryset,
		}
	return render(request, "inicio.html", context)


def contact(request):
	titulo = "Contacta con nosotros"
	form = ContactForm(request.POST or None)
	if form.is_valid():
		#for key in form.cleaned_data:
		#	print (key)
		#	print (form.cleaned_data.get(key))
		form_email = form.cleaned_data.get("email")
		form_mensaje = form.cleaned_data.get("mensaje")
		form_nombre = form.cleaned_data.get("nombre")
		asunto = 'Form de Contacto'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		mensaje_email = "%s : %s enviado por %s" %(form_nombre, form_mensaje, form_email)
		send_mail(asunto,
			mensaje_email,
			email_from,
			email_to,
			fail_silently=False #si lo dejamos en False , veremos el error para el texting , en true , aunque este mal no nos saldra el error
			)
		#print (email, mensaje, nombre)

	context = {
		"form" : form,
		"titulo" : titulo,
	}

	return render(request, "forms.html", context)








