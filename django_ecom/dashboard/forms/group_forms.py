from django import forms
from django.contrib.auth.models import Group


class GroupCreateForm(forms.ModelForm):
		name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))

		class Meta:
			model=Group
			fields=[
				'name'
			]