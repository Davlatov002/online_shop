from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
    path('category/',views.categoriy, name='category' ),
    path('category-creted/',views.categoriy_created, name='category' ),
    path('category-get-id/<str:pk>/',views.categoriy_id, name='category-get-id'),
    path('category-update/<str:pk>/',views.categoriy_update, name='category-update' ),
    path('category-delete/<str:pk>/',views.categoriy_delete, name='category-delete' ),
    path('praduct/',views.praduct, name='praduct' ),
    path('praduct-get-id/<str:pk>/',views.praduct_id, name='praduct-get-id'),
    path('praduct-creted/',views.praduct_created, name='category' ),
    path('praduct-update/<str:pk>/',views.praduct_update, name='praduct-update' ),
    path('praduct-delete/<str:pk>/',views.praduct_delete, name='praduct-delete' ),
    path('expired/',views.expired, name='expired' ), 
    path('shop-sell-total/',views.shop_sell_total, name='shop-sell-total' ), 
    path('best-selling-product/',views.best_selling_product, name='best-selling-product' ), 
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
