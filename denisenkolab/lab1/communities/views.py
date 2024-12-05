from django.shortcuts import render
from .models import Community

def communities_list(req):
    communities = Community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html',  {'communities': communities})

def community_page(request, slug):
    communities = Community.objects.get(slug=slug)
    return render(request, 'communities/community_page.html', {'communities': communities})
# Create your views here.
