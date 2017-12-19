from django import forms
from django.contrib.auth.models import User

USER_CHOICES = (
    ('unknown', 'Select Type'),
    (1, "Super User"),
    (0, "Stuff")
)

class UserForm(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':False}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required': False}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	is_superuser=forms.ChoiceField(choices = USER_CHOICES,widget=forms.Select(attrs={'class':'form-control','required': True}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))
	# confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))

	def __init__(self, *args, **kwargs):
		super(UserForm,self).__init__(*args, **kwargs)
		attrs={'class':'form-control','required': True}
		if self.instance and self.instance.pk:
			self.fields.pop('password', None)
		for field in self.fields.values():
			field.widget.attrs = attrs

	class Meta:
		model=User
		fields=['email','first_name','last_name','username','password','is_superuser']
		

	def save(self,commit=True):
		# email = self.cleaned_data['email'] 
		# print User.objects.get(email=email)
		# newUser = User.objects.get(email=email)

		# if newUser and newUser.email != self.cleaned_data['email']:
		# 	raise forms.ValidationError("please this email already exists")

		user=super(UserForm,self).save(commit=False)
		print user.id;

		if not self.instance:
			user.set_password(self.cleaned_data['password'])
		if commit and self.is_valid():
			user.save()
		return user	


class UserEditForm(forms.ModelForm):
	# username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required':False}))
	email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control','required': False}))
	first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
	is_superuser=forms.ChoiceField(choices = USER_CHOICES,widget=forms.Select(attrs={'class':'form-control','required': True})) 
	# password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))
	# confirm_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','required': False}))

	# def __init__(self, *args, **kwargs):
	# 	super(UserForm, self).__init__(*args, **kwargs)
	# 	# assign a (computed, I assume) default value to the choice field
	# 	self.initial['is_superuser'] = '1'

	class Meta:
		model=User
		fields=['email','first_name','last_name','is_superuser']
		

	def save(self,commit=True):
		email = self.cleaned_data['email'] 
		newUser = User.objects.get(email=email)
		# print self

		if newUser and newUser.email != self.cleaned_data['email']:
			raise forms.ValidationError("please this email already exists")

		user=super(UserEditForm,self).save(commit=False)
		print user.id;

		# user.set_password(self.cleaned_data['password'])
		if commit and self.is_valid():
			user.save()
		return user	











