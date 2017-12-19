from django import forms

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)

User=get_user_model()

class LoginForm(forms.Form):

		username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))

		def clean(self, *args, **kwargs):

			username=self.cleaned_data.get('username')
			password=self.cleaned_data.get('password')

			if username and password:
				print('after clean')
				user = authenticate(username=username,password=password)
				if not user:
					raise forms.ValidationError('User does not exist')
				if not user.is_active:
					raise forms.ValidationError('Sorry you are not active')
				if not user.check_password(password):
					raise forms.ValidationError('Incorrect password')
			return super(LoginForm,self).clean(*args,**kwargs)

