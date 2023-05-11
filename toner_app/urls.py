from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('select_toner/', views.select_toner, name='select_toner'),
    path('confirm_toner/<int:toner_id>/', views.confirm_toner, name='confirm_toner'),
    path('toner/list/', views.toner_list, name='toner_list'),
    path('subtract_toner/', views.subtract_toner, name='subtract_toner'),
    path('index/', views.index, name='index'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
