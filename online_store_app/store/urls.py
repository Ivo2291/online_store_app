from rest_framework_nested import routers

from online_store_app.store import views as v

router = routers.DefaultRouter()
router.register('products', v.ProductViewSet, basename='products')
router.register('collections', v.CollectionViewSet)
router.register('carts', v.CartViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', v.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls
