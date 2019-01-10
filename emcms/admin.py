from django.contrib import admin

# Register your models here.
from . models import Categories
from . models import Shop
from . models import Pic
from datetime import datetime
from django.utils.html import format_html
from django.contrib.contenttypes.admin import GenericTabularInline
#from django.utils.safestring import mark_safe
#https://docs.djangoproject.com/en/1.9/ref/contrib/admin/

admin.site.site_header = 'EM CMS'
class CategoriesAdmin(admin.ModelAdmin):
    def test_obj(self,obj):
        print('------selected = %s'%obj.Floor)
        return "xxxxxxxx"

    test_obj.short_description = "Test"
    exclude = ('create_by','updated_by','Create_date','updated_date')
    search_fields = ['Cat_Name']
    fields = ('Cat_Name','Parent_ID','Cat_Level','Active','Test','Floor','test_obj')
    readonly_fields = ('test_obj',)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        print('------------call change_view')
        return self.changeform_view(request, object_id, form_url, extra_context)
    def formfield_for_choice_field(self, db_field, request, **kwargs):
        print('------------call formfield_for_choice_field')
        return super().formfield_for_choice_field(db_field, request, **kwargs)
    def save_model(self, request, obj, form, change):
        if(not obj.create_by_id):
            obj.create_by = request.user
            obj.Create_date = datetime.now()
        obj.updated_by = request.user
        obj.updated_date = datetime.now()
        print('--------save = %d %s %s' % (obj.Create_date.day, request.user,obj.Floor))
        print("------------------Admin Category save")
        super().save_model(request, obj, form, change)

admin.site.register(Categories,CategoriesAdmin)
#admin.site.register(Category)
class ShopAdmin(admin.ModelAdmin):
    def cover_image(self, obj):
        return format_html('<img src="{}" />'.format(obj.cover.url))
    def icon_image(self, obj):
        return format_html('<img src="{}" />'.format(obj.icon.url))
    cover_image.short_description = 'Cover Image'
    icon_image.short_description = 'Icon Image'
    #actions_on_top = False
    #list_display = ('Shop_Name','Shop_Detail_TH','icon','cover')
    def get_thai_name(self,obj):
        return  obj.Shop_ShortName_TH

    #get_thai_name.short_description = "ชื่อไทย"
    list_display = ('get_thai_name','Shop_ShortName_EN', 'Shop_Detail_TH','Shop_Detail_EN', 'icon_image','cover_image','Email','Floor','Tel','Branch_Code','pivot_icon','x_pivot','y_pivot','Create_date','Create_by','Updated_date','Updated_by')
    search_fields = ['Shop_Name','category__Cat_Name']

    exclude = ('Create_by','Updated_by','Updated_date','Create_date','Shop_ID')
    def save_model(self, request, obj, form, change):
        if(not obj.Create_by_id):
            obj.Create_by = request.user
            obj.Create_date = datetime.now()
        else:
            print('--------------- aready created %s'%request.user)
        obj.Updated_by= request.user
        obj.Updated_date = datetime.now()
        if(obj.pk is not None):
            print('----------------------obj pk = %d'%obj.id)
        else:
            print('-----------obj is none')
        super().save_model(request, obj, form, change)

admin.site.register(Shop,ShopAdmin)
#admin.site.register(Shop)
#add cancel button admin site
#https://stackoverflow.com/questions/7587872/django-cancel-button-for-form-in-admin-site

# link custom flied value https://stackoverflow.com/questions/41632215/django-auto-assign-a-value-to-a-model-field-on-save-in-admin
#custom search https://www.reddit.com/r/django/comments/3i432y/decorate_the_word_search_in_admin/


#detect field data changed
#https://stackoverflow.com/questions/1197674/actions-triggered-by-field-change-in-django
#https://code.i-harness.com/en/q/14ad8e
#https://www.netlandish.com/blog/2013/12/14/easily-track-data-changes-in-your-django-models/