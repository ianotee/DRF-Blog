from django.contrib import admin
from .models import Person

admin.site.site_header ="DRF_Blog"

class PersonAdmin(admin.ModelAdmin):
    list_display =['name','age']
    list_filter =['name']
    search_fields =['name']
    





admin.site.register(Person)
