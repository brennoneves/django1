from django.shortcuts import render

from .models import Produto
# passar os parametros para os templates e
def index(request):
     produtos = Produto.objects.all()
     print(request.user)
     teste=''
     if str(request.user) == 'AnonymousUser':
          teste ='Usuario nao logado'
     else:
          teste=f'usuario logado como: {request.user}'
     context = {
          'curso':'Programacao Web com Django',
          'outro': 'Django é bom mesmo heimm..',
          'user':f'{request.user} : seja bem vindo',
          'logado':teste,
          'produtos':produtos
     }
     return render(request, 'index.html',context)

def contato(request):
     return render(request, 'contato.html')

def produto(request,id):
     prod = Produto.objects.get(id=id)
     context ={
          'produto':prod
     }
     print(f'PK: {id}')
     return render(request, 'produto.html',context)