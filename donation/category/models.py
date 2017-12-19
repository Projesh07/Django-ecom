from django.db import models
from datetime import datetime


#Image Uploade for category function

def uplaod_location(instance,filename):
	return "%s/%s%s.%s" %('documents',instance.id,instance.id,filename)

class Category(models.Model):
		
		name=models.CharField(max_length=120)
		image=models.ImageField(upload_to=uplaod_location,height_field="height_field",
			width_field="width_field",null=True,blank=True)
		
		descriptions=models.TextField(null=True)
		height_field=models.IntegerField(default=0,null=True,blank=True)
		width_field=models.IntegerField(default=0,null=True,blank=True)
		created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
		updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

		class Meta:
			db_table ='categories'

		def __str__(self):
			return self.name    

