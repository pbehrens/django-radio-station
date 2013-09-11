# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from radio.content.models import Post
from django.shortcuts import render_to_response
from django.template import loader, RequestContext
from django.http import Http404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from radio.logs.models import Entry


def detail(request, post_id):
	try:
		p = Post.objects.get(pk=post_id).order_by('-pub_date')
	except Post.DoesNotExist:
		raise Http404
	latest_logs = Entry.objects.all().order_by('-submitted')[0:10]
	
	ctxt = {
        'logs':latest_logs,
		'post':p,
    }
	
		
	return render_to_response('detail.html', ctxt, context_instance=RequestContext(request))
		
def index(request):
	posts = Post.objects.all().order_by('-pub_date')
	paginator = Paginator(posts, 10)
	try: page = int(request.GET.get("page", '1'))
	except ValueError: page = 1

	try:
		posts = paginator.page(page)
	except (InvalidPage, EmptyPage):
		posts = paginator.page(paginator.num_pages)
	
	latest_logs = Entry.objects.all().order_by('-submitted')[0:10]
	ctxt = {
        'logs':latest_logs,
		'posts':posts,
    }
	return render_to_response("index.html", dict(posts=posts), context_instance=RequestContext(request))
 



	
