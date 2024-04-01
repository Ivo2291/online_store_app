from rest_framework_nested import routers

from online_store_app.store import views as v

router = routers.DefaultRouter()
router.register('products', v.ProductViewSet)
router.register('collections', v.CollectionViewSet)

products_router = routers.NestedDefaultRouter(router, 'products', lookup='product')
products_router.register('reviews', v.ReviewViewSet, basename='product-reviews')

urlpatterns = router.urls + products_router.urls
