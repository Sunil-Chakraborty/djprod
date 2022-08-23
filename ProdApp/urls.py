from django.urls import path
from . import views

app_name = 'ProdApp'

urlpatterns = [   
    path('', views.index, name='index'),   
    path('prod-view/', views.prod_view, name='prod-view'),
    path('create-prod/', views.create_Prod, name="create-prod"),
    #path('edit-prod/<str:pk>/', views.editProd, name="edit-prod"),
    #path('delete-prod/<str:pk>/', views.deleteProd, name="delete-prod"),
]
