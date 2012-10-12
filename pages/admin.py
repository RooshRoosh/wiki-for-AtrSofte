from django.contrib import admin
from models import *
class PageAdmin(admin.ModelAdmin):
    list_display=('title','text','slug')
admin.site.register( Page,PageAdmin)
