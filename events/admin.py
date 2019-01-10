from django.contrib import admin

# Register your models here.
from . models import Category
from . models import Shop
from . models import Pic
from datetime import datetime
from django.contrib.contenttypes.admin import GenericTabularInline
#from django.utils.safestring import mark_safe

class CategoryAdmin(admin.ModelAdmin):
    pass
    exclude = ('create_by','updated_by')
    def save_model(self, request, obj, form, change):
        if(not obj.create_by_id):
            obj.create_by = request.user
            obj.Create_date = datetime.now()
        obj.updated_by = request.user
        obj.updated_date = datetime.now()
        print("------------------Admin Category save")
        #print('--------save = %d %s' % (obj.Create_date.day, request.user))

        super().save_model(request, obj, form, change)
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        print("-----db_field = %s",db_field)
        return super().formfield_for_choice_field(db_field, request, **kwargs)


admin.site.register(Category,CategoryAdmin)
#admin.site.register(Category)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ['Shop_Name']
    def save_model(self, request, obj, form, change):
        #print('--------save = %d',obj.Create_date)
        obj.save()

    def formfield_for_choice_field(self, db_field, request, **kwargs):

        return super().formfield_for_choice_field(db_field, request, **kwargs)
admin.site.register(Shop,ShopAdmin)
admin.site.site_header = 'Em Cms'
class PicAdmin(admin.ModelAdmin):
    list_display = ('pic',)
    search_fields = ['shop_pic']
    def pic(self, obj):  # receives the instance as an argument
        return '<img src="{thumb}" />'.format(
            thumb=obj.shop_pic.url,
        )
        pic.allow_tags = True
        pic.short_description = 'sometext'
admin.site.register(Pic,PicAdmin)
#admin.site.register(Pic)
