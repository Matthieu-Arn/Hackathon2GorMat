from django.urls import path
from . import views

urlpatterns = [
    path('', indexpage, name='index'),
    path('create/', views.create_item_view, name='create_item'),
    path('', views.item_list_view, name='item_list'),
    path('<int:item_id>/recovered/', views.mark_as_recovered_view, name='mark_as_recovered'),
    path('<int:item_id>/comment/', views.add_comment_view, name='add_comment'),
]
