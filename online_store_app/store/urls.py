from django.urls import path

from online_store_app.store import views as v

urlpatterns = (
    path('products/', v.products_list, name='products_list'),
    path('products/<int:pk>/', v.product_details, name='product_details'),
    path('collections/', v.collection_list, name='collection_list'),
    path('collections/<int:pk>/', v.collection_details, name='collection_details'),
)

