from django.shortcuts import render

def communities(req):
    return render(req, 'communities/communities.html')

# Create your views here.
