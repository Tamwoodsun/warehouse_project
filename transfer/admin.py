from django.contrib import admin
from .models import Transfer
# Register your models here.

class TransferAdmin(admin.ModelAdmin):
    list_display = ('id','user','is_active','warehouse','rent_date', 'rent_date','end_date')
    list_display_links = ('id','user')
    list_filter = ('rent_date',)
    list_editable = ('is_active','rent_date','end_date')
    search_fields = ('user','warehouse',)
    list_per_page = 25

admin.site.register( Transfer, TransferAdmin)