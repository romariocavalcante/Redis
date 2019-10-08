from django.shortcuts import render
from .models import herois

#@cache_page(60) #tempo de vida do cache
def home(request):
	#import pdb;pdb.set_trace()
	lista = herois.objects.all()
	return render(request,'conteudo.html', {'lista':lista})
'''
	form = PostForm()
	if(request.method == 'POST'):
		form = PostForm(request.POST)
		if(form.is_valid()):
			post_nome = form.cleaned_data['nome']
			post_universo = form.cleaned_data['universo']
			post_habilidade = form.cleaned_data['habilidade']
			new_post = Post(nome=post_nome, universo=post_universo, habilidade=post_habilidade )
			new_post.save()
			return redirect('')
	elif(request.method == 'GET'):	

'''
	


    
        