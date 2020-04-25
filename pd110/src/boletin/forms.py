from django import forms


from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]

	def clean_email(self):
		email =  self.cleaned_data.get("email")
		email_base, proveeder = email.split("@")
		dominio, extension = proveeder.split(".")
		if not extension == "edu":
			raise forms.ValidationError("Por favor utiliza un correo del IES Fernando Aguilar")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#Validaciones
		return nombre

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)

	#def clean_email(self):
	#	email =  self.cleaned_data.get("email")
	#	email_base, proveeder = email.split("@")
		#dominio, extension = proveeder.split(".")
	#		if not email_base and proveeder == "iesfernandoaguilar.es":
	#		raise forms.ValidationError("Utiliza otro correo")
	#	return email