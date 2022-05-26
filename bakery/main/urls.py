from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<page_name>', views.show_page)
]
