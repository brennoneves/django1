from django.shortcuts import render
# passar os parametros para os templates e
def index(request):
     context = {
          'curso':'Programacao Web com Django',
          'outro': 'Django é bom mesmo heimm..'
     }
     return render(request, 'index.html',context)

def contato(request):
     return render(request, 'contato.html')