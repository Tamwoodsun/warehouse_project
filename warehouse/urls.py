from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('<int:warehouse_id>/', views.warehouse_one, name='warehouse'),
    path('<int:warehouse_id>', views.warehouse_one, name='warehouse_no_slash'), 
    path('',views.warehouse, name="warehouse"),
    path('<str:region_name>', views.show_region, name='region'),
    #path('<slug>', views.show_region_slug, name='region_slug' )
    path('processorder', views.processorder, name="processorder")

]
