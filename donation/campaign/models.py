from django.db import models
from datetime import datetime
from category.models import Category
from django.contrib.auth.models import User
from django.db.models import Sum
from django.conf import settings
from django.conf.urls.static import static

from django.template.defaultfilters import slugify



# class CampaignStatusManager(models.Manager):
#     def active(self):
#         return super(CampaignStatusManager, self).get_queryset().filter(status=1)

# 	def inactive(self):
# 		return super(CampaignStatusManager, self).get_queryset().filter(status=0)

# tag model class
class Tag(models.Model):
	
	name = models.CharField(
    	max_length=255,
    )

	created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

	class Meta:
		db_table ='tag'
	def __str__(self):
		return self.name
		
class Campaign(models.Model):
	
	def total_donate(self):
		#calculate total donated amount
		totalAmount = 0.0
		all_donate = Donate.objects.filter(campaign_id=self.id)

		for donate_val in all_donate:
			print donate_val.amount
			totalAmount += donate_val.amount
		return totalAmount
	
	# def get_document(self):
	# 	docs=Documents.objects.filter(campaign_id=self.id)

	# 	content=list()
	# 	# print document_file

	# 	if docs:
	# 		for doc_file in docs:
	# 			if doc_file.content_type !='link':
	# 				content.append(settings.BASE_URL+doc_file.content)
	# 	return content			

	

	def progress(self):
		# progress = amount *(total_donate/100)
		return 100

	tags = models.ManyToManyField(Tag) 
	title=models.CharField(max_length=255)
	slug = models.SlugField(null=True)
	story=models.TextField(null=True)		
	amount=models.FloatField(default=0.0)
	start_date=models.DateField(auto_now=False,auto_now_add=False)
	end_date=models.DateField(auto_now=False,auto_now_add=False)
	publish_date=models.DateTimeField(auto_now=False,auto_now_add=True)
	status=models.IntegerField(default=0)
	category = models.ForeignKey(Category, models.SET_NULL, blank=True, null=True)
	created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

	class Meta:
		db_table ='campaign'
	def __str__(self):
		return self.title 

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super(Campaign, self).save(*args, **kwargs)

def uplaod_location(instance,filename):
	return "%s/%s%s.%s" %('documents',instance.id,instance.id,filename)

class Documents(models.Model):
	
	FILE_TYPE_CHOICES = (
        ('image', 'Image'),
        ('file', 'File'),
        ('video', 'Video'),
        ('link', 'Link'),
    )

	def url(self):
		if self.content_type !='link':
					return settings.BASE_URL+self.content
		else:
			return self.content


    
	content=models.CharField(max_length=255,null=True,blank=True)
	content_type = models.CharField(
    	max_length=255,
        choices=FILE_TYPE_CHOICES,
        default='image',
    )
	campaign = models.ForeignKey(Campaign, models.SET_NULL, blank=True, null=True, related_name="documents")
	created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)
	
	class Meta:
		db_table ='documents'
	# def __str__(self):
	# 	return self.content


#comments model class
class Comments(models.Model):
	
	user 		= models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name="comment_user")
	campaign 	= models.ForeignKey(Campaign, models.SET_NULL, blank=True, null=True, related_name="campaign_comment")
	
	comment 	= models.TextField()
	comment_at 	= models.DateTimeField(auto_now=False,auto_now_add=True)
	created_at	=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_at	=models.DateTimeField(auto_now=True,auto_now_add=False)

	class Meta:
		db_table ='comments'
	def __str__(self):
		return self.comment
	

class Donate(models.Model):
	
	user 		= models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name="donate_user")
	campaign 	= models.ForeignKey(Campaign, models.SET_NULL, blank=True, null=True, related_name="campaign_donates")
	
	amount 	= models.FloatField(default=0.0)
	donate_at 	= models.DateTimeField(auto_now=False,auto_now_add=True)
	created_at	=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_at	=models.DateTimeField(auto_now=True,auto_now_add=False)

	class Meta:
		db_table ='donate'
	# def __str__(self):
	# 	return self.amount 
	