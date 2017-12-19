from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views.generic import ListView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from dashboard.forms.user_forms import UserForm
from dashboard.forms.user_forms import UserEditForm

from dashboard.tables.tables import AdminUserTable
from django.db.models import Q
from table.views import FeedDataView 



# class Admin():

# 	def user_group(self, *args,**kwargs):
# 		group=Group.objects.all()
# 		return group

# 	def users(self, *args,**kwargs):
# 		users=User.objects.all()
# 		return users	

#.......................................


# User list view

class UserList(ListView):
	model = User

	template_name='admin/user_list.html'
	def get_context_data(self,**kwargs):
		page_title="User List"
		context=super(UserList,self).get_context_data(**kwargs)
		context['users']=User.objects.all()
		context['title']=page_title
		context['admin_table']=AdminUserTable(User.objects.all().filter(Q(is_superuser=1) | Q(is_staff=1)))

		return context

class UserTableList(FeedDataView):
	
        token = AdminUserTable.token
        
        def get_queryset(self):
            return super(UserTableList, self).get_queryset()
            

class UserCreate(CreateView):
	template_name='admin/user_crud_form.html'
	form_class=UserForm

	def get_context_data(self,**kwargs):
		context=super(UserCreate,self).get_context_data(**kwargs)
		context['title']="Admin Create"
		return context

	def get_success_url(self):
		return reverse('list_user')

class UserUpdate(UpdateView):
	template_name='admin/user_crud_form.html'
	# model = User
	form_class=UserForm

	def get_context_data(self,**kwargs):
		context=super(UserUpdate,self).get_context_data(**kwargs)
		context['title']="User Update"
		return context
	
	def get_object(self):
		user = User.objects.get(id=self.kwargs['id'])
		return user
	
	def get_form(self, **kwargs):
		# if request.user.is_staff: # condition
		user = self.get_object()
		if user.is_superuser:
			self.initial['is_superuser'] = 1
		else:
			self.initial['is_superuser'] = 2

		print self.get_object().is_superuser

		# self.exclude = ('password',)
		return super(UserUpdate, self).get_form(**kwargs)

	def post(self, request, *args, **kwargs):
		print self.request 

		self.object = self.get_object()
		form = self.get_form()
		email = self.request.POST.get('email')
		newUser = User.objects.get(email=email)

		if newUser and newUser.id != self.object.id:
			raise form.ValidationError('please this email already exists')

		# if form.is_valid():

		view = super(UserUpdate, self).post(request, *args, **kwargs)
		# print view
		return view

	def get_success_url(self):
		isAdmin = self.request.POST.get('is_superuser')
		print 'lol'
		if isAdmin == '1':
			return reverse('list_user')
		else:
			return reverse('list_site_user')

		

class UserDelete(DeleteView):
	template_name='admin/user_confirm_delete.html'
	form_class=UserForm

	def get_context_data(self,**kwargs):
		context=super(UserDelete,self).get_context_data(**kwargs)
		context['title']="User Delete"
		return context

	def get_object(self):
		user = User.objects.get(id=self.kwargs['id'])
		if self.request.user.id == user.id:
			user.same_user = True;
		else:
			user.same_user = False;
		return user

	def delete(self,request, *args, **kwargs):
		self.object = self.get_object()
		if self.request.user.id == self.object.id:
			raise Exception('you can not delete yourself')
		# success_url = self.get_success_url()
		self.object.delete()
		# user = self.object.id
		print self.object.is_superuser

		# isAdmin = User.objects.filter(id=user,is_superuser=1)
		# print success_url
		if self.object.is_superuser :
			success_url = reverse('list_user')			
		else:
			success_url = reverse('list_site_user')
		
		return HttpResponseRedirect(success_url)

	def get_success_url(self):
		return reverse('list_user')
