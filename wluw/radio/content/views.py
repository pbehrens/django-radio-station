# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from radio.content.models import Post
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage


def detail(request, post_id):
	try:
		p = Post.objects.get(pk=post_id)
	except Post.DoesNotExist:
		raise Http404
		
	return render_to_response('detail.html', {'post': p})
		
def index(request):
	posts = Post.objects.all()
	paginator = Paginator(posts, 2)
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)

	return render_to_response("index.html", dict(posts=posts))
 



	
