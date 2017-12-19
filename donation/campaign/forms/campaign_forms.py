from django import forms
from campaign.models import Campaign,Tag,Documents
from category.models import Category

class CampaignForm(forms.ModelForm):

		title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': False,'placeholder': 'Name of the Campaign to be created'}))
		story=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','required': False,'rows': 12,'placeholder': 'whiteout the detailed story about the campaign'}))
		amount=forms.FloatField(max_value=1000000, min_value=0, widget=forms.NumberInput(attrs={'class':'form-control', 'step': "0.01",'required':False}))
		category=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Select Category',widget=forms.Select(attrs={'label':'Select','class':'form-control','required': False}))
		# tags=forms.MultipleChoiceField(widget=forms.TextInput(attrs={'class':'form-control','required': False}))
		# tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple(attrs={'class':'','name':'tags','type':'hidden'}))
		
		start_date=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','required': True,'placeholder': 'start date','data-date-format': 'yyyy-mm-dd'}))
		end_date=forms.CharField(widget = forms.TextInput(attrs={'class':'form-control','required': True,'placeholder': 'end date','data-date-format': 'yyyy-mm-dd'}))
		
		class Meta:
			model=Campaign
			# fields=('category','tags' ,'title','story','amount',"start_date","end_date")
			fields=('category','title','story','amount',"start_date","end_date",)
			


class CampaignForm2(forms.ModelForm):
		content_type = forms.ChoiceField(choices=Documents.FILE_TYPE_CHOICES,widget=forms.Select(attrs={'label':'Select','class':'form-control'}))
		class Meta:
			model=Documents
		# fields=('category','title','story','amount',"start_date","end_date")
			fields=('content_type',)
		
				
