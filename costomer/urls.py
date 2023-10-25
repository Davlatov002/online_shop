from django.urls import path
from . import views

urlpatterns = [
    path('costomer/',views.costomer, name='category' ),
    path('costomer-get-id/<str:pk>/',views.costomer_id, name='costomer-get-id' ),
    path('costomer-creted/',views.costomer_created, name='costomer-created' ),
    path('costomer-update/<str:pk>/',views.costomer_update, name='costomer-update' ),
    path('costomer-delete/<str:pk>/',views.costomer_delete, name='costomer-delete' ),
    path('shopcard/',views.shopcard, name='shopcard' ),
    path('shopcard-get-id/<str:pk>/',views.shopcard_id, name='shopcard-get-id' ),
    path('shopcard-creted/',views.shopcard_created, name='shopcard-creted' ),
    path('shopcard-update/<str:pk>/',views.shopcard_update, name='shopcard-update' ),
    path('shopcard-delete/<str:pk>/',views.shopcard_delete, name='shopcard-delete' ),
    path('all-purchases/<str:pk>/',views.all_purchases, name='all-purchases' ),  
    path('the-purchase-price/<str:pk>/',views.the_purchase_price, name='the-purchase-price' ),  
]
