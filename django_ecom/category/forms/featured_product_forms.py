from django import forms
from category.models import FeaturedProduct,Product

class FeaturedProductForm(forms.ModelForm):

		note=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','required': False}))
		product=forms.ModelChoiceField(queryset=Product.objects.all(),empty_label='Select Product',widget=forms.Select(attrs={'class':'form-control','required': False}))
		class Meta:
			model=FeaturedProduct
			fields=('product','note')