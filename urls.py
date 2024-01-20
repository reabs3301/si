from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('table_produits/',views.afficher_table , name = 'list_produit'),
    path('add_product/<str:type>',views.add_product , name='add_product'),
    path('select_product/<int:id>/<str:type>',views.select , name = 'select_product'),
    path('edit_product/<int:id>/<str:type>',views.modify_product , name = 'edit'),
    path('delete_product/<int:id>/<str:type>',views.delete_product , name = 'delete'),
    path('search_product/',views.search_product , name = 'search_product'),
    path('choose_add/',views.choosing , name='choose'),
    path('details_centre/<int:id>',views.details , name='details'),
    path('add_vente/',views.add_vente , name='add_vente'),
    path('table_team/<int:id>',views.afficher_team , name = 'list_team'),
    path('select_team/<int:id>',views.select_team , name = 'select_team'),
    path('pointage/<int:id>',views.pointage , name = 'pointage'),
    path('emprunt/<int:id>',views.emprunt , name = 'emprunt'),
]
