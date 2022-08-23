from django.urls import path

from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('home1',views.home1, name='home1'),
    path('delete',views.delete,name='delete'),
    path('edit',views.edit,name='edit'),
    path('update',views.update,name='update'),
    
]