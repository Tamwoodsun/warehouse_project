from django.contrib import admin
from .models import Warehouse
# Register your models here.

class WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id','title','region','district','floor','room','description','phone','main_img','img1','img2','threemonrent','sixmonrent','ninemonrent','is_listed')
    list_display_links = ('id','title')
    list_filter = ('region',)
    list_editable = ('is_listed',)
    search_fields = ('title','region','district',)
    list_per_page = 25
    #prepopulated_fields = {"slug": ("region","title")}
    
admin.site.register( Warehouse, WarehouseAdmin)    