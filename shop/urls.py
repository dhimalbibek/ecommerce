from django.urls import path 
from shop.views import create_form,read_view,update_view,delete_view

urlpatterns = [
    path('create/', create_form),
    path('read/<int:id>/', read_view,name='read'),
    path('update/<int:id>/', update_view,name='update'),
    path('delete/<int:id>/', delete_view, name='delete'),
]