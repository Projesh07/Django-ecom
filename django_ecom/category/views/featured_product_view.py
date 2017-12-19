from django.shortcuts import render
from django.views.generic import ListView
from category.models import FeaturedProduct,Product
from django.core.urlresolvers import reverse

from category.forms.featured_product_forms import FeaturedProductForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class FeaturedProductList(ListView):

	model=FeaturedProduct
	template_name='product/featured_product_list.html'

	def get_context_data(self,**kwargs):
		page_title="Featured Product add"
		context=super(FeaturedProductList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		context['title']=page_title
		context['url_create']='create_featured_product'
		context['url_delete']='delete_featured_product'
		context['url_update']='update_featured_product'
		form_val=self.request.GET.get('search')
		
		if form_val:
			context['featured_products']=FeaturedProduct.objects.filter(product__name__icontains=form_val)
		else:	
			context['featured_products']=FeaturedProduct.objects.all()	
		return context




class FeaturedProductCreate(CreateView):
		template_name='product/crud_form.html'
		# model = Group
		# fields =['name']
		form_class=FeaturedProductForm
		
		def get_success_url(self):
			return reverse('list_featured_product')
class FeaturedProductUpdate(UpdateView):

		template_name='product/crud_form.html'
		form_class=FeaturedProductForm
		def get_object(self, **kwargs):
			return FeaturedProduct.objects.get(id=self.kwargs['id'])
		def get_success_url(self,**kwargs):
			return reverse('list_featured_product')
								
class FeaturedProductDelete(DeleteView):

		template_name='product/delete_confirm.html'

		form_class=FeaturedProductForm
		def get_object(self,**kwargs):

			return FeaturedProduct.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_featured_product')
