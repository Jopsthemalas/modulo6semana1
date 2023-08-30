from django.contrib import admin
from django.contrib import messages

from base.models import Contato

@admin.action (description='marcar formulario como lido')
def marcar_como_lido (modeladmin ,request ,queryset):
    queryset.update (lido=True)
    modeladmin.menssage_user(request ,'marcar formulario como lido',messages.SUCCESS )
    
 
@admin.register(Contato)
class ContatoAdmin (admin.ModelAdmin):
    list_display = ['nome','email',]
    search_fields = ['nome','email']
    list_filter = ['nome','lido']
    actions = [marcar_como_lido]