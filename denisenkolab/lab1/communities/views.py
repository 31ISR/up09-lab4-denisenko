from django.shortcuts import render
from .models import Community
from django.contrib.auth.decorators import login_required

def communities_list(req):
    communities = Community.objects.all().order_by('-date')
    return render(req, 'communities/communities_list.html',  {'communities': communities})

def communities_page(request, slug):
    community = Community.objects.get(slug=slug)
    return render(request, 'communities/communities_page.html', {'community': community})
# Create your views here.


@login_required(login_url="/users/login/")
def post_new(request):
    return render(request, 'communities/community_new.html')