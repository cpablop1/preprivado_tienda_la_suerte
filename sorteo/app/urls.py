from django.urls import path
from . import views

app_name = 'sistema'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('clientes/', views.gestion_clientes, name='gestion_clientes'),
    path('venta/', views.realizar_venta, name='realizar_venta'),
    path('venta/<int:venta_id>/voucher/', views.voucher_venta, name='voucher_venta'),
    path('resultados/', views.registrar_resultado, name='resultados_sorteo'),
    path('reportes/ganadores/', views.reporte_ganadores, name='reporte_ganadores'),
    path('reportes/recaudacion/', views.reporte_recaudacion, name='reporte_recaudacion'),
]