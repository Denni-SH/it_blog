from django import forms
from .models import CustomUser


class SignForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = '__all__'
