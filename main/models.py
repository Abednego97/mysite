from django.db import models
from datetime import datetime


# Create your models here.


class Category(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category

class Series(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(Category, default = 1,verbose_name="Category", on_delete=models.SET_DEFAULT)
	series_summary = models.CharField(max_length= 200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series

class Tutorial(models.Model):
	Tut_Tittle= models.CharField(max_length=200)
	Tut_Content= models.TextField()
	Tut_Date = models.DateTimeField('date published',default=datetime.now())
	tutorial_series = models.ForeignKey(Series, default = 1, verbose_name="Series",on_delete=models.SET_DEFAULT)
	tutorial_slug = models.CharField(max_length=200,default= 1)

	def __str__(self):
			return self.Tut_Tittle