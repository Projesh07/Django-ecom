from django import forms
from category.models import Menu

class MenuForm(forms.ModelForm):

		name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		descriptions=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','required': False}))

		class Meta:
			model=Menu
			fields=('name','descriptions','image')