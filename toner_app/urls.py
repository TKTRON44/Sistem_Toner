from django.contrib import admin
from django.urls import path
from . import views
from .views import toner_list

urlpatterns = [
    path('', views.home, name='home'),
    path('select_toner/', views.select_toner, name='select_toner'),
    path('confirm_toner/<int:toner_id>/', views.confirm_toner, name='confirm_toner'),
    path('retirada_devolucao/', views.retirada_devolucao, name='retirada_devolucao'),
    path('toner/list/', toner_list, name='toner_list'), # nova rota
     path('index/', views.index, name='index'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
