from django.shortcuts import render
from django.views.generic import ListView
from category.models import Product
from django.core.urlresolvers import reverse

from category.forms.product_forms import ProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class ProductList(ListView):

	model=Product
	template_name='product/product_list.html'

	def get_context_data(self,**kwargs):
		page_title="Product add"
		context=super(ProductList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		context['title']=page_title
		context['url_create']='create_product'
		context['url_delete']='delete_product'
		context['url_update']='update_product'
		form_val=self.request.GET.get('search')

		if form_val:
			context['products']=Product.objects.filter(name__icontains=form_val)
		else:	
			context['products']=Product.objects.all()	
		return context




class ProductCreate(CreateView):
		template_name='product/crud_form.html'
		# model = Group
		# fields =['name']
		form_class=ProductForm
		
		def get_success_url(self):
			return reverse('list_product')
class ProductUpdate(UpdateView):

		template_name='product/crud_form.html'
		form_class=ProductForm
		def get_object(self, **kwargs):
			return Product.objects.get(id=self.kwargs['id'])
		def get_success_url(self,**kwargs):
			return reverse('list_product')
								
class ProductDelete(DeleteView):

		template_name='product/delete_confirm.html'

		form_class=ProductForm
		def get_object(self,**kwargs):

			return Product.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_product')
