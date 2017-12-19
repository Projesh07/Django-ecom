from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.views.generic import TemplateView
from dashboard.forms.group_forms import GroupCreateForm 
from dashboard.forms.user_forms import UserCreateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.core.urlresolvers import reverse
class Admin(TemplateView):
	"""docstring for ClassName"""
	def user_group(self, *args,**kwargs):
		group=Group.objects.all()
		return group

	def users(self, *args,**kwargs):
		users=User.objects.all()
		return users

	def user_permission(self,*args,**kwargs):
		permissions=Permission.objects.all()
		return permissions

#This is admin crud view

class AdminCreate(CreateView):
		template_name='dashboard/user/crud_form.html'
		# model = Group
		# fields =['name']
		form_class=GroupCreateForm
		
		def get_success_url(self):
			return reverse('list_group')

class AdminUpdate(UpdateView):
		model = Group
		fields =['name']

class AdminDelete(DeleteView):
	model = Group

class AdminGroupList(ListView):
	model = Group
	
	template_name='admin/group_list.html'
	def get_context_data(self,**kwargs):
		page_title='Group add'
		context=super(AdminGroupList,self).get_context_data(**kwargs)
		context['groups']=Group.objects.all()
		context['title']=page_title
		return context


class UserCreate(CreateView):
		template_name='dashboard/user/crud_form.html'
		# model = Group
		# fields =['name']
		form_class=UserCreateForm
		
		def get_success_url(self):
			return reverse('list_user')

class UserUpdate(UpdateView):
		template_name='dashboard/user/crud_form.html'

		form_class=UserCreateForm
		def get_object(self):

			return User.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_user')

class UserDelete(DeleteView):
		template_name='dashboard/user/delete_confirm.html'

		form_class=UserCreateForm
		def get_object(self):

			return User.objects.get(id=self.kwargs['id'])

		def get_success_url(self):
			return reverse('list_user')

class UserList(ListView):
	model = User

	template_name='admin/user_list.html'
	def get_context_data(self,**kwargs):
		page_title="User add"
		context=super(UserList,self).get_context_data(**kwargs)
		context['users']=User.objects.all()
		context['title']=page_title
		return context



	




		
		