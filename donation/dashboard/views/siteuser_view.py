from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.views.generic import ListView,TemplateView
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from dashboard.forms.user_forms import UserForm
from django.shortcuts import redirect

from dashboard.tables.tables import AdminUserTable
from dashboard.tables.tables import SiteUserTable
from table.views import FeedDataView
	
class SiteUser():

	def user_group(self, *args,**kwargs):
		group=Group.objects.all()
		return group

	def users(self, *args,**kwargs):
		users=User.objects.all()
		return users	

class SiteUserList(ListView):
	model = User

	template_name='user/user_list.html'

	def get_context_data(self,**kwargs):
		page_title="Site User List"
		context=super(SiteUserList,self).get_context_data(**kwargs)
		context['users']=User.objects.all()
		context['title']=page_title
		context['admin_table']=SiteUserTable(User.objects.filter(is_superuser=0,is_staff=0))

		return context

class SiteUserTableList(FeedDataView):
	
        token = SiteUserTable.token
        
        def get_queryset(self):
            return super(SiteUserTableList, self).get_queryset()

class SiteUserCreate(CreateView):

	template_name='admin/user_crud_form.html'
	form_class=UserForm

	def get_success_url(self):
		return reverse('list_site_user')

class SiteUserUpdate(UpdateView):

	template_name='admin/user_crud_form.html'
	form_class=UserForm

	def get_object(self):
		return User.objects.get(id=self.kwargs['id'])
	def get_success_url(self):
		return reverse('list_site_user')
		

class SiteUserDelete(DeleteView):

	template_name='admin/user_crud_form.html'
	form_class=UserForm

	def get_object(self):
		return User.objects.get(id=self.kwargs['id'])
	def get_success_url(self):
		return reverse('list_site_user')

class SiteUserStatus(TemplateView):

		template_name='admin/confirm_status.html'

		def get_context_data(self,**kwargs):

			context = super(SiteUserStatus, self).get_context_data(**kwargs)
			context['title']='User Status'
			context['user_status'] = User.objects.get(id=self.kwargs['id'])	
			if self.request.user.id == context['user_status'].id:
				context['same_user'] = True;
			else:
				context['same_user'] = False;
			# print context['user_status'].id
			return context		

	
		def post(self, request, *args, **kwargs):
			user_status=User.objects.get(id=self.kwargs['id'])

			if user_status.is_active==0:
	
				user_status.is_active=1
			else:

				user_status.is_active=0

			user_status.save()

			return redirect('list_site_user')		

		def get_success_url(self):
			return reverse('list_site_user')			


		