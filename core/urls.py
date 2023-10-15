from django.urls import path
from core.views import * 


urlpatterns = [
    path('home/', index, name='index'),
    path('home/<str:nombre_usuario>/', index2, name='nombre_usuario'),
    path('especialidades_listado/', especialidades_listado, name='especialidades_listado'),
    path('medicos/', medicos, name='medicos'),
    path('datos_personales_medico/<int:matricula>', datos_personales_medico, name="datos_personales_medico"),
    path('carga/',carga_medico, name='carga_medico'),
    path('alta', alta_medico, name = 'alta_medico')
]