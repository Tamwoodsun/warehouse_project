from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','is_active', 'creation_date', 'email','phone','first_name','last_name')
    list_display_links = ('id',)
    list_filter = ('username',)
    list_editable = ('is_active','username','first_name','last_name')
    search_fields = ()
    list_per_page = 25
    
admin.site.register(User, UserAdmin)    