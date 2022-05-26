from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration', views.registration),
    path('admin', admin.site.urls),
    # path('<page_name>', views.show_page)
]
