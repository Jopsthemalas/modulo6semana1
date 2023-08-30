from django.urls import path
from rest_api.views import contato,contato_envio, contato_delete

app_name = 'rest_api'

urlpatterns = [
   path ('contato_api',contato,name = 'hello_word_api' ),
   path ('envio',contato_envio,name ='envio_api' ),
   path ('delete',contato_delete, name='delete_api')
]