from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response 
from base.models import Contato

@api_view()

def contato (request):
    consulta = Contato.objects.all()
    dados = []
    for informacao in consulta :

        dado = {
                 'id' : informacao.id ,
                 'nome' :informacao.nome ,
                'email' : informacao.email ,
                'mensagem' : informacao.mensagem,




        }

        dados.append(dado)
    return Response (dados)

@api_view(http_method_names=['POST'])

def contato_envio (request):
    
    nome =request.data['nome']
    email = request.data ['email']
    mensagem = request.data ['mensagem']

    contato = Contato.objects.create(nome=nome ,email=email,mensagem=mensagem)
    dado = {
                 'id' :contato.id ,
                 'nome' :contato.nome ,
                 'email' : contato.email ,
                 'mensagem' : contato.mensagem,

    }
    return Response (dado)
    
@api_view(http_method_names=['DELETE'])

def contato_delete (request):
    
    nome =request.data['nome']
    email = request.data ['email']
    mensagem = request.data ['mensagem']

    contato = Contato.objects.delete(nome=nome ,email=email,mensagem=mensagem)
    dado = {
                 'id' :contato.id ,
                 'nome' :contato.nome ,
                 'email' : contato.email ,
                 'mensagem' : contato.mensagem,

    }
    return Response (dado)