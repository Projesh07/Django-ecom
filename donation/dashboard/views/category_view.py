
from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from category.models import Category
from django.core.urlresolvers import reverse

from dashboard.tables.tables import CategoryTable

from category.forms.category_forms import CategoryForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from table.views import FeedDataView 


class CategoryList(TemplateView):

	def get(self, request, *args, **kwargs):
		page_title="Category List"
		context=super(CategoryList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		context['title']=page_title
		context['url_create']='create_category'
		context['url_delete']='delete_category'
		context['url_update']='update_category'
		form_val=self.request.GET.get('search')

		# if form_val:
		# 	context['categories']=Category.objects.filter(name__icontains=form_val)
		# else:
		# 	# pass
		# 	context['categories']=Category.objects.all()
		
		context['categories']=CategoryTable()
		# return context
		return render(request,"category/category_list.html",context)	

class CategoryTableList(FeedDataView):

        token = CategoryTable.token

        def get_queryset(self):
            return super(CategoryTableList, self).get_queryset()		


class CategoryCreate(CreateView):
		template_name='category/crud_form.html'
		# model = Group
		# fields =['name']
		form_class=CategoryForm

		def get_success_url(self):
			return reverse('list_category')
			
class CategoryUpdate(UpdateView):

		template_name='category/crud_form.html'
		form_class=CategoryForm
		def get_object(self, **kwargs):
			return Category.objects.get(id=self.kwargs['id'])
		def get_success_url(self,**kwargs):
			return reverse('list_category')

class CategoryDelete(DeleteView):

		template_name='category/delete_confirm.html'

		form_class=CategoryForm
		def get_object(self,**kwargs):

			return Category.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_category')
