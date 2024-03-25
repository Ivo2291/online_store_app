from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Online Store Admin'
admin.site.index_title = 'Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('online_store_app.store.urls')),
]
