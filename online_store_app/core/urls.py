from django.urls import path

from online_store_app.core import views as v

urlpatterns = (
    path('', v.index, name='index'),
)
