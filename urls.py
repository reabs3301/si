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
    path('produits_affichage/<int:id>',views.afficher_produit , name = 'produits_affichage'),
    path('produits_profit/<int:id>/<int:id2>',views.profits , name = 'produits_profit'),
    path('dash_board/<int:id>',views.dash_board , name = 'dash_board'),
    path('dash_board2/<int:id>',views.dash_board2 , name = 'dash_board2'),
]
