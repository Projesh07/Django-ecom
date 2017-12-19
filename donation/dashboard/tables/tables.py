from campaign.models import Donate
from category.models import Category
from campaign.models import Campaign
from django.contrib.auth.models import User
from table import Table
from table.columns import DatetimeColumn,Column,LinkColumn,Link
from table.columns.imagecolumn import ImageColumn
from table.utils import A
from table.utils import Accessor
from django.template import Template, Context
from django.shortcuts import get_list_or_404, get_object_or_404
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse_lazy


class ImageColumnChange(ImageColumn):
		# def __init__(self):
		# 	ImageColumn.__init__(self)

		def render(self, obj):
			path = Accessor(self.field).resolve(obj)
			print self
			if isinstance(self.image_title, Accessor):
				title = self.image_title.resolve(self.obj)
			else:
				title = self.image_title
			template = Template('{%% load static %%}<img style="width:30px;height:30px;"src="{%% static "../../%s" %%}"'
			' title="%s">' % (path, title))
			return template.render(Context())

class LinkColumnStatus(Link):

    def render(self, obj):
        """ Render link as HTML output tag <a>.
        """
        self.obj = obj
        # print self.obj.status
        if self.obj.status ==1:
        	text_change='toggle-on'	
        	t_class = 'tick'
        else:
        	text_change='toggle-off'
        	t_class = 'cross'
        attrs = ' '.join([
            '%s="%s"' % (attr_name, attr.resolve(obj))
            if isinstance(attr, Accessor)
            else '%s="%s"' % (attr_name, attr)
            for attr_name, attr in self.attrs.items()
        ])


        return mark_safe(u'<a %s><i class="fa fa-%s %s" aria-hidden="true" ></i></a>' % (attrs, text_change, t_class))

class AssertiveColumn(Column):

    def render(self, obj):
        """ Render value as Yes/No
        """
        self.obj = obj
        # print self.obj.status
        if self.obj.is_superuser == 1:
        	text_change='check'
        	t_class = 'tick'
        else:
        	text_change='times'	
        	t_class = 'cross'
       


        return mark_safe(u'<i class="fa fa-%s %s" aria-hidden="true" ></i>' % (text_change,t_class))


class LinkColumnAccess(Link):

    def render(self, obj):

        self.obj = obj

        if self.obj.is_active==1:

        	text_change='ban'
        	t_class = 'cross'
        else:
        	text_change='unlock'	
        	t_class = 'tick'

        attrs = ' '.join([
            '%s="%s"' % (attr_name, attr.resolve(obj))
            if isinstance(attr, Accessor)
            else '%s="%s"' % (attr_name, attr)
            for attr_name, attr in self.attrs.items()
        ])


        return mark_safe(u'<a %s><i class="fa fa-%s %s" aria-hidden="true" ></i></a>' % (attrs, text_change, t_class))

class LinkColumnUpdate(Link):

	def render(self, obj):

		self.obj = obj

		text_change = 'pencil-square-o'
		t_class = 'grey'

		attrs = ' '.join([
		    '%s="%s"' % (attr_name, attr.resolve(obj))
		    if isinstance(attr, Accessor)
		    else '%s="%s"' % (attr_name, attr)
		    for attr_name, attr in self.attrs.items()
		])


		return mark_safe(u'<a %s><i class="fa fa-%s %s" aria-hidden="true" ></i></a>' % (attrs, text_change, t_class))

class LinkColumnDelete(Link):

    def render(self, obj):

		self.obj = obj

		text_change = 'trash'
		t_class = 'cross'

		attrs = ' '.join([
		'%s="%s"' % (attr_name, attr.resolve(obj))
		if isinstance(attr, Accessor)
		else '%s="%s"' % (attr_name, attr)
		for attr_name, attr in self.attrs.items()
		])

		return mark_safe(u'<a %s><i class="fa fa-%s %s" aria-hidden="true" ></i></a>' % (attrs, text_change, t_class))

class LinkColumnDetails(Link):

	def render(self, obj):

		self.obj = obj
		text_change = 'eye'
		t_class = 'grey'

		attrs = ' '.join([
			'%s="%s"' % (attr_name, attr.resolve(obj))
			if isinstance(attr, Accessor)
			else '%s="%s"' % (attr_name, attr)
			for attr_name, attr in self.attrs.items()
		])

		return mark_safe(u'<a %s><i class="fa fa-%s %s" aria-hidden="true" ></i></a>' % (attrs, text_change, t_class))




class CategoryTable(Table,ImageColumnChange):

	name=Column(field='name',header='Name')
	image=ImageColumnChange(field='image.url',header='Image',image_title='image')

	descriptions=Column(field='descriptions',header='Descriptions')

	created_at=Column(field='created_at',header='Create Date')
	updated_at=DatetimeColumn(field='updated_at',header='Update date',format='%d-%m-%Y %H:%I:%S')
	Action=LinkColumn(header='Action', links=[
		LinkColumnDelete(viewname='delete_category', args=(A('id'),), text='Delete'),
		LinkColumnUpdate(viewname='update_category', args=(A('id'),), text='Update')])


	class Meta:
		model = Category
		ajax = True
		ajax_source = reverse_lazy('category_table_data')


class CampaignTable(Table,LinkColumnStatus):

	title=Column(field='title',header='Title',)
	# story=Column(field='story',header='Story',)
	amount=Column(field='amount',header='Amount',)
	# status=Column(field=get_status(id),header='Status',)

	end_date=Column(field='end_date',header='End Date',)
	publish_date=Column(field='publish_date',header='Publish date',)

	
	Action=LinkColumn(header='Action', links=[
		LinkColumnDetails(viewname='campaign_details', args=(A('id'),), text='Details status'),
		LinkColumnStatus(viewname='campaign_status', args=(A('id'),), text='Change status'),
		LinkColumnUpdate(viewname='update_campaign', args=(A('id'),), text='Update'),
		LinkColumnDelete(viewname='delete_campaign', args=(A('id'),), text='Delete'),
	])

	class Meta:
		model = Campaign
		ajax = True
		ajax_source = reverse_lazy('ajax_campaign_table_data')

#Datatable 
class AdminUserTable(Table):

	first_name=Column(field='first_name',header='First name',)
	last_name=Column(field='last_name',header='Last name',)
	username=Column(field='username',header='Username')
	email=Column(field='email',header='Email')
	is_superuser=AssertiveColumn(field='is_superuser',header='Is SuperUser')

	Action=LinkColumn(header='Action', links=[
	LinkColumnDelete(viewname='delete_user', args=(A('id'),), text='Delete'),
	LinkColumnUpdate(viewname='update_user', args=(A('id'),), text='Update'),
	LinkColumnAccess(viewname='access_status', args=(A('id'),), text='Access change')])


	class Meta:
		model = User
		ajax = True
		ajax_source = reverse_lazy('ajax_user_table_data')

class SiteUserTable(Table):

	first_name=Column(field='first_name',header='First name',)
	last_name=Column(field='last_name',header='Last name',)
	username=Column(field='username',header='Username')
	email=Column(field='email',header='Email')
	# is_superuser=AssertiveColumn(field='is_superuser',header='Is SuperUser')

	Action=LinkColumn(header='Action', links=[
	LinkColumnDelete(viewname='delete_user', args=(A('id'),), text='Delete'),
	# Link(viewname='update_user', args=(A('id'),), text='Update'),
	LinkColumnAccess(viewname='access_status', args=(A('id'),), text='Access change')])


	class Meta:
		model = User
		ajax = True
		ajax_source = reverse_lazy('ajax_site_user_table_data')		

class PaymentTable(Table):

	user=Column(field='user.username',header='User')
	campaign=Column(field='campaign.title',header='Campaign')
	amount=Column(field='amount',header='Amount')

	Action=LinkColumn(header='Action', links=[
	LinkColumnDelete(viewname='delete_user', args=(A('id'),), text='Delete'),
	# Link(viewname='update_user', args=(A('id'),), text='Update'),
	# LinkColumnAccess(viewname='access_status', args=(A('id'),), text='Access change')
	])


	class Meta:
		model = Donate		
		ajax = True
		ajax_source = reverse_lazy('ajax_payment_table_data')


