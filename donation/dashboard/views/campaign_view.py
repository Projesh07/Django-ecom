# Create your views here.
from formtools.wizard.views import SessionWizardView
from django.shortcuts import render_to_response
from django.shortcuts import redirect
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


from django.shortcuts import render,HttpResponseRedirect
from django.views.generic import ListView,TemplateView,DetailView
from campaign.models import Campaign,Tag,Documents,Category,Donate
from django.core.urlresolvers import reverse

from campaign.forms.campaign_forms import CampaignForm,CampaignForm2
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import json
from django.http import JsonResponse, HttpResponse
from dashboard.tables.tables import CampaignTable,PaymentTable
from django.template.defaultfilters import slugify
from table.views import FeedDataView
import datetime


class CampaignList(ListView):
	model=Campaign
	template_name='dashboard/campaign/campaign_list.html'

	def get_context_data(self,**kwargs):
		context=super(CampaignList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		page_title="Campaign List"
		context['title']=page_title
		context['url_create']='create_campaign'
		context['url_delete']='delete_campaign'
		context['url_update']='update_campaign'
		form_val=self.request.GET.get('search')
		context['campaign_table']=CampaignTable()

		# print settings.MEDIA_URL
		print datetime.datetime.now().strftime('%Y%m%d%h%s')

		if form_val:
			context['campaignes']=Campaign.objects.filter(title__icontains=form_val)
		else:
			context['campaignes']=Campaign.objects.all()
		return context

		def get_success_url(self):
			return reverse('list_campaign')

class CampaignTableList(FeedDataView):

    token = CampaignTable.token

    def get_queryset(self):
        return super(CampaignTableList, self).get_queryset()	

class CampaignCreate(TemplateView):
	# form_list = [CampaignForm]
	# template_name='campaign/crud.html'
	template_name='campaign/campaign_create.html'
	form_class = CampaignForm

	# /media_cdn/documents/

	def post(self, request, *args, **kwargs):
		context = self.get_context_data()
		context['form'] = CampaignForm(self.request.POST,self.request.FILES or None);
		links =self.request.POST.getlist('link[]')
		# documents= self.request.POST.getlist('document[]') request.FILES['file']
		documents= self.request.FILES.getlist('document[]')
		images= self.request.FILES.getlist('image[]')
		tags=self.request.POST.getlist('tags_val[]')
		

		if context["form"].is_valid():

			print 'trying to be slugy'
			# context["form"].fields.slug = slugify(self.request.POST.get('title'))
			
			context["form"].save(commit=False)
			campaign=context["form"].save()
			c_id=campaign.id

			if links is not None:
				for link in links:				
					content_type='link'
					Documents.objects.create(content=link,content_type=content_type,campaign_id=c_id)
			
			if documents is not None:
				for document in documents:
					content_type='file'
					dirname=settings.MEDIA_ROOT + '/documents/campaign-file'

					if os.path.exists(dirname):
						pass

					else:
						os.mkdir(os.path.join('/file', dirname))

					fs = FileSystemStorage(location=dirname)

					ext = document.name.split('.')
					ext = ext[ len(ext) - 1 ]
				
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-file/'+ file_name
					
				
					fname=fs.save(file_name,document)
					
					# uploaded_file_url='documents/campaign-file/'+document.name				
					
					Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			
			
			if images is not None:

				for image in images:
					content_type='image'
					dirname=settings.MEDIA_ROOT + '/documents/campaign-image'
			

					if os.path.exists(dirname):
						pass

					else:
						os.mkdir(os.path.join('/image', dirname))

					fs = FileSystemStorage(location=dirname)
				
					ext = image.name.split('.')
					ext = ext[ len(ext) - 1 ]
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') +"."+ ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-image/'+ file_name
								
					fname=fs.save(file_name,image)
					Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			



			if tags is not None:
				for tag in tags:

					if not tag.isnumeric():
						new_tag = Tag.objects.create(name=tag)
						campaign.tags.add(new_tag)
					else:
						tag = Tag.objects.get(id=tag)
						campaign.tags.add(tag)

			return redirect('list_campaign')		


		return super(CampaignCreate, self).render_to_response(context)


	def get_context_data(self, **kwargs):
		context = super(CampaignCreate, self).get_context_data(**kwargs)
		
		page_title="Campaign Create"
		context['title']=page_title

		form = CampaignForm()  # instance= None
	
		tag_db=Tag.objects.all()
		context["form"] = form
		context['tags']=tag_db

		return context

	def render_to_response(self, context, **response_kwargs):

		if self.request.is_ajax():
			tag=self.request.GET.get('select_val')
			# if not Tag.objects.filter(name=tag).exists():
			# 	Tag.objects.create(name=tag)	
			return JsonResponse(json.dumps(tag),safe=False, **response_kwargs)
		else:
			return super(CampaignCreate,self).render_to_response(context, **response_kwargs)


class AJAXDocumentDelete(TemplateView):

	template_name=None

	def post(self, request, *args, **kwargs):
		response_data={}
		if self.request.is_ajax():
			file_id = request.POST.get('file_id')
			
			if Documents.objects.filter(id=file_id).exists():
				file = Documents.objects.get(id=file_id)
				Documents.objects.filter(id=file_id).delete()
				response_data['success'] = True
				from django.core import serializers
				# unlink( settings.MEDIA_ROOT + file.content )
				try:
				    os.remove(settings.MEDIA_ROOT + file.content)
				except OSError:
				    pass
				# response_data['file']=serializers.serialize('json', [file])
				# response_data['file']=json.dumps(file)
				response_data['file_path']=json.dumps(settings.MEDIA_ROOT + file.content)
			else:
				response_data['success'] = False
		else:
			response_data['success'] = False
		return HttpResponse(json.dumps(response_data), content_type="application/json")	
	# def render_to_response(self, context, **response_kwargs):

	# 	if self.request.is_ajax():
	# 		file_id = self.request.POST.get('file_id')
	# 		if Document.objects.filter(id=file_id).exists():
	# 			file = Document.objects.filter(id=file_id)
	# 			print file
	# 			response_data={}
	# 			response_data['success'] = True
	# 			response_data['file']=file
	# 			return HttpResponse(json.dumps(response_data), content_type="application/json")
	# 		else:
	# 			return JsonResponse(json.dumps([('supccess', False) ]),safe=False, **response_kwargs)
	# 	else:
	# 		return JsonResponse(json.dumps([('succesis', False) ]),safe=False, **response_kwargs)

	

class CampaignUpdate(TemplateView):

	template_name='campaign/campaign_update.html'

	def get_context_data(self,**kwargs):

		context = super(CampaignUpdate, self).get_context_data(**kwargs)
		camp=Campaign.objects.get(id=self.kwargs['id'])
		form = CampaignForm(self.request.POST or None,self.request.FILES or None,instance=camp)  # instance= None
		context["form"] = form

		page_title="Campaign Update"
		context['title']=page_title

		context['campaign']=camp
		tag=camp.tags.all()

		context['documents']=Documents.objects.filter(campaign_id=self.kwargs['id'])


		context["camp_tags"]=tag
		context["tags"] =Tag.objects.all()
		
		return context

	def post(self, request, *args, **kwargs):

		context = self.get_context_data()
		links =self.request.POST.getlist('link[]')
		documents= self.request.FILES.getlist('document[]')
		
		images= self.request.FILES.getlist('image[]')

		tags=self.request.POST.getlist('tags_val[]')

		print context["form"].is_valid()
		

		if context["form"].is_valid():
			
			context["form"].save(commit=False)
			# print context["form"].fields.slug
			campaign=context["form"].save()
			c_id=campaign.id

			# deleting existing links for restore.. 
			Documents.objects.filter(campaign_id=c_id,content_type='link').delete()

			if links is not None:
				for link in links:
				
					content_type='link'
					Documents.objects.create(content=link,content_type=content_type,campaign_id=c_id)
			
			if documents is not None:
				for document in documents:
					content_type='file'
					dirname=settings.MEDIA_ROOT + '/documents/campaign-file'
					# print document.type

					if os.path.exists(dirname):
						pass

					else:
						os.mkdir(os.path.join('/file', dirname))

					fs = FileSystemStorage(location=dirname)

					ext = document.name.split('.')
					ext = ext[ len(ext) - 1 ]
				
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') + "." + ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-file/'+ file_name
					
					fname=fs.save(file_name,document)

					# print 'test : ' + fname


				
					Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			
			
			if images is not None:
				for image in images:
					content_type='image'
					dirname=settings.MEDIA_ROOT + '/documents/campaign-image'

					if os.path.exists(dirname):
						pass

					else:
						os.mkdir(os.path.join('/image', dirname))

					fs = FileSystemStorage(location=dirname)

					ext = image.name.split('.')
					ext = ext[ len(ext) - 1 ]
					file_name = str(c_id) + datetime.datetime.now().strftime('%Y%m%d%h%s') +"."+ ext
					uploaded_file_url= settings.MEDIA_URL +  'documents/campaign-image/'+ file_name
					
				
					fname=fs.save(file_name,image)
					
					Documents.objects.create(content=uploaded_file_url,content_type=content_type,campaign_id=c_id)			



			if tags is not None:
				for tag in tags:

					if not tag.isnumeric():
						new_tag = Tag.objects.create(name=tag)
						campaign.tags.add(new_tag)
					else:
						tag = Tag.objects.get(id=tag)
						campaign.tags.add(tag)	


			return redirect('list_campaign')		


		return super(CampaignUpdate, self).render_to_response(context)


		def get_success_url(self,**kwargs):
			return reverse('list_campaign')

class CampaignDelete(DeleteView):

		template_name='campaign/confirm_delete.html'
		title = 'Campaign Delete'

		form_class=CampaignForm
		def get_object(self,**kwargs):

			return Campaign.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_campaign')

class CampaignStatus(TemplateView):

		template_name='campaign/confirm_status.html'
		# model=Campaign
		def get_context_data(self,**kwargs):

			context = super(CampaignStatus, self).get_context_data(**kwargs)
			context['campaign']=Campaign.objects.get(id=self.kwargs['id'])	
			context['title']="Change Status"

			return context		

	
		def post(self, request, *args, **kwargs):
			campaigns=Campaign.objects.get(id=self.kwargs['id'])

			if campaigns.status==0:
	
				campaigns.status=1
			else:

				campaigns.status=0
	
			campaigns.save()

			return redirect('list_campaign')



		def get_success_url(self):
			return reverse('list_campaign')			

class CampaignDetails(DetailView):
    model = Campaign
    template_name = 'campaign/campaign_detail_view.html'


    def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(CampaignDetails, self).get_context_data(**kwargs)
		page_title="Campaign Details"
		context['title']=page_title
		print context['campaign'].id

		context['documents']=Documents.objects.filter(campaign_id=context['campaign'].id)

		# context["tags"] =Tag.objects.all()
		# print context
		# context['now'] = timezone.now()
		return context		

class PaymentList(ListView):
	model = Donate
	template_name='donate/payment_list.html'

	def get_context_data(self,**kwargs):
		page_title="Payment List"
		context=super(PaymentList,self).get_context_data(**kwargs)
		# context['users']=User.objects.all()
		if self.kwargs and self.kwargs['user']:
			data = Donate.objects.filter(user_id=self.kwargs['user'])
		elif self.kwargs and self.kwargs['campaign']:
			data = Donate.objects.filter(campaign_id=self.kwargs['campaign'])
		else: 
			data = Donate.objects.all()
		context['title']=page_title
		context['payment_table']=PaymentTable(data)

		return context

class PaymentTableList(FeedDataView):

    token = PaymentTable.token

    def get_queryset(self):
        return super(PaymentTableList, self).get_queryset()	


