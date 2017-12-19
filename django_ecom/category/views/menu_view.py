from django.shortcuts import render
from django.views.generic import ListView
from category.models import Menu
from django.core.urlresolvers import reverse

from category.forms.menu_forms import MenuForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class MenuList(ListView):
	template_name='template_name'
	model=Menu
	template_name='dashboard/category/menu_list.html'

	def get_context_data(self,**kwargs):
		page_title="Menu add"
		context=super(MenuList,self).get_context_data(**kwargs)
		# context['categories']=Category.objects.all()
		context['title']=page_title
		context['url_create']='create_menu'
		context['url_delete']='delete_menu'
		context['url_update']='update_menu'
		form_val=self.request.GET.get('search')

		if form_val:
			context['menus']=Menu.objects.filter(name__icontains=form_val)
		else:	
			context['menus']=Menu.objects.all()	
		return context




class MenuCreate(CreateView):
		template_name='category/crud_form.html'
		# model = Group
		# fields =['name']
		form_class=MenuForm
		
		def get_success_url(self):
			return reverse('list_menu')
class MenuUpdate(UpdateView):

		template_name='category/crud_form.html'
		form_class=MenuForm
		def get_object(self, **kwargs):
			return Menu.objects.get(id=self.kwargs['id'])
		def get_success_url(self,**kwargs):
			return reverse('list_menu')
								
class MenuDelete(DeleteView):

		template_name='category/delete_confirm.html'

		form_class=MenuForm
		def get_object(self,**kwargs):

			return Menu.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_menu')
