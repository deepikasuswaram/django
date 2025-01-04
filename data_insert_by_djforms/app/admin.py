from django.contrib import admin
from app.models import *
# Register your models here.

class WebpageAdminView(admin.ModelAdmin):
    list_display=['topic_name','name','url','email']
    list_editable=('name',)
    list_per_page=3
    list_display_links=['url']
    search_fields=['name']
    list_filter=['url','name','topic_name']
    

class AR_AdminView(admin.ModelAdmin):
    list_display=['name','author','date']
    




admin.site.register(Topic)
admin.site.register(Webpage,WebpageAdminView)
admin.site.register(AccessRecord,AR_AdminView)

admin.site.site_header='Django'
admin.site.site_title='DJD-M3'
admin.site.index_title='PROJECT'