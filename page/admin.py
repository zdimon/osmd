from django.contrib import admin
from page.models import *
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Page, PageAdmin)





class PhotoInline(admin.TabularInline):
    list_display = ("name","image" )
    model = Photo


class SubjectAdmin(admin.ModelAdmin):
    inlines = [ PhotoInline, ]

admin.site.register(Subject, SubjectAdmin)
