from django import forms
from category.models import Product,Category,Menu

class ProductForm(forms.ModelForm):

		name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		descriptions=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','required': False}))
		sell_price=forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control','required': False}))
		category=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Select Category',widget=forms.Select(attrs={'label':'Select','class':'form-control','required': False}))
		menu=forms.ModelChoiceField(queryset=Menu.objects.all(),empty_label='Select Menu',widget=forms.Select(attrs={'class':'form-control','required': False}))
		class Meta:
			model=Product
			fields=('category','menu','name','descriptions','sell_price','image')