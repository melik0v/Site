from django.urls import path
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    # path('', views.index),
    path('admin', admin.site.urls),
    # path('<page_name>', views.show_page)
    url(r'^product/(?P<product_id>\w+)/$', views.product, name='product')
]
