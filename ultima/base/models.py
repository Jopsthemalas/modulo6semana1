from django.db import models

class Contato (models.Model):
    nome = models.CharField (verbose_name='nome', max_length=50)
    email = models.EmailField (verbose_name='email', max_length = 50)
    mensagem = models.TextField (verbose_name= 'mensagem')
    lido = models.BooleanField (verbose_name='lido',default= False ,blank= True)
    def __str__(self):
        return f'{self.nome} [{self.email}]'
    class meta :
       verbose_name ='formulario contato'
       verbo_name_plural ='formulario contatos'
       ordering = ['nome']