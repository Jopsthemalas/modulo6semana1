from django.shortcuts import render
from base.forms import ContatoForm


def inicio (request):
 return  render (request,'inicio.html')

def contato (request):
   sucesso = False
   form = ContatoForm (request.POST or None)
   if form.is_valid():
     form.save()
     sucesso = True
   contexto = { 'telefone':'(99)99999-9999',
              'responsavel': 'Maria da Silva Pereira',
               'form':form,
                'sucessso': sucesso
               }
 

   return render (request,'contato.html',contexto)