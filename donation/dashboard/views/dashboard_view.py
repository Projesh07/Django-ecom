
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.views.generic import TemplateView
from django.views import View
from django.conf import settings

from django.contrib.auth.models import User

from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout
	)
class DashboardView(TemplateView):

	template_name='dashboard/dashboard.html'
	
	def get_context_data(self,**kwargs):
		user=User.objects.all()
		context = super(DashboardView, self).get_context_data(**kwargs)
		context['data'] =user
		
		return context