from django.db import models
# from djmoney.models.fields import MoneyField 

# Create your models here.

# class CategoryManager(models.Manager):
def uplaod_location(instance,filename):
	return "%s/%s%s.%s" %('documents',instance.id,instance.id,filename)

class Category(models.Model):
		
		name=models.CharField(max_length=120)
		image=models.ImageField(upload_to=uplaod_location,height_field="height_field",
			width_field="width_field",null=True,blank=True)
		descriptions=models.TextField()
		height_field=models.IntegerField(default=0)
		width_field=models.IntegerField(default=0)
		created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
		updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

		class Meta:
			db_table ='categories'
		def __str__(self):
			return self.name
        			

		# objects= CategoryManager()


class Menu(models.Model):
		
		name=models.CharField(max_length=120)
		image=models.ImageField(upload_to=uplaod_location,height_field="height_field",
			width_field="width_field",null=True,blank=True)
		descriptions=models.TextField()
		height_field=models.IntegerField(default=0)
		width_field=models.IntegerField(default=0)
		created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
		updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

		class Meta:
			db_table ='menus'
		def __str__(self):
			return self.name
					

		# objects= CategoryManager()
# reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

class Product(models.Model):
		category=models.ForeignKey(Category, on_delete=models.CASCADE)
		menu=models.ForeignKey(Menu,on_delete=models.CASCADE)
		name=models.CharField(max_length=120)
		image=models.ImageField(upload_to=uplaod_location,height_field="height_field",
			width_field="width_field",null=True,blank=True)
		sell_price=models.DecimalField(max_digits=8,default=0,decimal_places=2)
		descriptions=models.TextField()
		height_field=models.IntegerField(default=0)
		width_field=models.IntegerField(default=0)
		created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
		updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

		class Meta:
			db_table ='products'
		def __str__(self):
			return self.name	



class FeaturedProduct(models.Model):
		product=models.ForeignKey(Product, on_delete=models.CASCADE)
		note=models.TextField()
		created_at=models.DateTimeField(auto_now=False,auto_now_add=True)
		updated_at=models.DateTimeField(auto_now=True,auto_now_add=False)

		class Meta:
			db_table ='featured_products'								
		
