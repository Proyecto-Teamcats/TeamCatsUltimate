from django.urls import path
from .views import home, form_persona, index, gale, login, nosotros, mantenedor, form_mod_gato, form_borrar_gato,\
                   ver_gatos, form_mod_persona, form_borrar_persona, ver_personas   
from .views import catalogo, form_gato


urlpatterns=[ 
    path('',home, name='home'),
    path('catalogo',catalogo, name='catalogo'),
    path('form_persona', form_persona, name='form_persona'),
    path('form_gato', form_gato, name='form_gato'),

    #Esto es de los gatos
    path('ver_gatos', ver_gatos, name='ver_gatos'),
    path('form_mod_gato/<id>', form_mod_gato, name='form_mod_gato'),
    path('form_borrar_gato/<id>', form_borrar_gato, name='form_borrar_gato'),

    #Esto es de las personas
    path('ver_personas', ver_personas, name='ver_personas'),
    path('form_mod_persona/<id>', form_mod_persona, name='form_mod_persona'),
    path('form_borrar_persona/<id>', form_borrar_persona, name='form_borrar_persona'),


    #Aqui van mis html normales de navegación
    path('index',index, name='index'),
    
    path('gale',gale, name='gale'),

    path('login',login, name='login'),

    path('nosotros',nosotros, name='nosotros'),

    path('mantenedor',mantenedor, name='mantenedor'),


]
