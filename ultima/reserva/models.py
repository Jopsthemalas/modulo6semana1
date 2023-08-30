from django.db import models

class Reserva (models.Model):
    TAMANHO_OPCAO = (
    (0, 'piqueno'),
    (1, 'médio'),
    (2, 'grande'),
    )
    TURNO_OPCAO = (

    ('manhã', 'manhã'),
    ('tarde' , 'tarde'),


    )

    nome = models.CharField (verbose_name='nome', max_length=50)
    email = models.EmailField (verbose_name='email', max_length = 50)
    nome_pet = models.CharField (verbose_name= 'nome do pet' ,max_length=50)
    data = models.DateField (verbose_name='data',help_text='dd/mm/aaaa')
    turno = models.CharField (verbose_name ='Turno',max_length=10 , choices=TURNO_OPCAO)
    tamanho = models.IntegerField (verbose_name= 'tamanho',choices=TAMANHO_OPCAO)
    observacoes = models.TextField (blank=True)

    def __str__ (self):
        return f'{self.nome}:{self.data}-{self.turno}'


    class meta :
        verbose_name ='Reserva de Banho'
        verbose_name_plural ='Reservas de banho'
