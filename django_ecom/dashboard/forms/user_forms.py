from django import forms
from django.contrib.auth.models import User

class UserCreateForm(forms.ModelForm):

		username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required': False}))
		first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))
		
		class Meta:
			model=User
			fields=('email','first_name','last_name','username','password')
		
		def save(self, commit=True):

			user=super(UserCreateForm,self).save(commit=False)
			user.set_password(self.cleaned_data["password"])
			if commit:
				user.save()
			return user
		def clean_password(self):
			return self.initial['password']		

