
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings
from .admin_view import Admin


from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)
class DashboardView(TemplateView):

	template_name='dashboard/dashboard.html'
	
	def get_context_data(self,**kwargs):
		
		context = super(DashboardView, self).get_context_data(**kwargs)
		context['groups'] = Admin.user_group(self)
		context['users'] = Admin.users(self)
		context['permissions'] = Admin.user_permission(self)
		return context

		