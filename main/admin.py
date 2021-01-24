from django.contrib import admin
from django.db import models
from .models import Tutorial,Category,Series
from tinymce.widgets import TinyMCE

class TutorialAdmin(admin.ModelAdmin):
	fieldsets=[
		("Tittle/Date",{'fields': ["Tut_Tittle","Tut_Date"]}),
		("URL",{'fields':["tutorial_slug"]}),
		("Series",{'fields':["tutorial_series"]}),
		("Content",{'fields': ["Tut_Content"]})
	]

	formfield_overrides ={
	models.TextField:{'widget':TinyMCE(attrs={'cols':80,'row':30})}
	}
	

# Register your models here.
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(Category)
admin.site.register(Series)
