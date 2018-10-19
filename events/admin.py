from django.contrib import admin

# Register your models here.
from . models import Category
from . models import Shop
from . models import Pic

from django.contrib.contenttypes.admin import GenericTabularInline
#from django.utils.safestring import mark_safe

admin.site.register(Category)
admin.site.register(Shop)
#class PicAdmin(admin.ModelAdmin):
#    list_display = ('pic',)
#    def pic(self, obj):  # receives the instance as an argument
#        return '<img src="{thumb}" />'.format(
#            thumb=obj.shop_pic.url,
#        )
#        pic.allow_tags = True
#        pic.short_description = 'sometext'
#admin.site.register(Pic,PicAdmin)
admin.site.register(Pic)
