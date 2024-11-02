from django.urls import path
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.base, name='base'),
   
    
    path('vendedor/',views.listar_vendedor,name='listar_vendedor'),
    path('vendedor/ver/<int:pk>/',views.ver_vendedor,name='ver_vendedor'),
    path('vendedor/crear',views.crear_vendedor,name='crear_vendedor'),
    path('vendedor/editar/<int:pk>/',views.editar_vendedor,name='editar_vendedor'),
    path('vendedor/eliminar/<int:pk>/',views.eliminar_vendedor,name='eliminar_vendedor'),
    
    path('cliente/',views.listar_cliente,name='listar_cliente'),
    path('cliente/crear/',views.crear_cliente,name='crear_cliente'),
    path('cliente/editar/<int:pk>/',views.editar_cliente,name='editar_cliente'),
    path('cliente/eliminar/<int:pk>/',views.eliminar_cliente,name='eliminar_cliente'),
    
    path('deportivo/',views.listar_deportivo,name='listar_deportivo'),
    path('deportivo/crear/',views.crear_deportivo,name='crear_deportivo'),
    path('deportivo/editar/<int:pk>/',views.editar_deportivo,name='editar_deportivo'),
    path('deportivo/eliminar/<int:pk>/',views.eliminar_deportivo,name='eliminar_deportivo'),
    
    
    path('compra/',views.listar_compra,name='listar_compra'),
    path('compra/crear/',views.crear_compra,name='crear_compra'),
    path('compra/editar/<int:pk>/',views.editar_compra,name='editar_compra'),
    path('compra/eliminar/<int:pk>/',views.eliminar_compra,name='eliminar_compra'),
    
    path('rol/',views.listar_roles,name='listar_rol'),
    path('rol/crear/',views.crear_rol,name='crear_rol'),
    path('rol/editar/<int:pk>/',views.editar_rol,name='editar_rol'),
    path('rol/eliminar/<int:pk>/',views.eliminar_rol,name='eliminar_rol'),
    
    path('usuario/',views.listar_usario,name='listar_usuario'),
    path('usuario/crear/',views.crear_usario,name='crear_usuario'),
    path('usuario/editar/<int:pk>/',views.editar_usuario,name='editar_usuario'),
    path('usuario/eliminar/<int:pk>/',views.eliminar_usuario,name='eliminar_usuario'),
    
    
    
    #Url Login y Logout
    path('accounts/login/',views.iniciar_sesion , name='login'),
    path('accounts/logot/',views.iniciar_sesion , name='logout'),
    
    
    #URL accesco denegado
    path('acceso_denegado/',views.acceso_denegado , name='acceso_denegado'),
    
   # URL Cambio de Contraseña
    path('cambiar_contraseña/', views.cambiar_contraseña, name='cambiar_contraseña'),
    
    
]+static(settings.MEDIA_URL,document_root =settings.MEDIA_ROOT)
