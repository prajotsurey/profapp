from django.shortcuts import render,redirect
from . import forms
from . models import Article
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
	return render(request,'articles/homepage.html')

@login_required(login_url = "accounts/login/")
def articleCreate(request):
	if request.method == 'POST':
		form  = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit = False)
			instance.author = request.user
			instance.save()
			return redirect('articles:yourlist')
	else:
		form = forms.CreateArticle()
	return render(request,'articles/article_create.html',{'form' : form})	

@login_required(login_url = "accounts/login/")	
def userArticles(request):
	articles = Article.objects.filter(author = request.user).order_by('-date')
	return render(request,'articles/user_articles.html',{'articles':articles})


def articleDetail(request,slug):
	article = Article.objects.get(slug = slug)
	return render(request,'articles/article_detail.html',{'article':article})

def publicArticles(request):
	articles = Article.objects.filter(private=False).order_by('-date')
	return	render(request,'articles/public_articles.html',{'articles':articles})