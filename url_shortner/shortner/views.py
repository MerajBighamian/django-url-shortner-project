from os import link
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Urls
import uuid
# Create your views here.

def index(request):
    return render(request,'shortner/index.html')

def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = Urls(links=url,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def return_orginal_url(request,uuid):
    orginal_url = Urls.objects.get(uuid=uuid)
    return redirect(orginal_url.links) 