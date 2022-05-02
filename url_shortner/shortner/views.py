from os import link
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Urls
import uuid
# Create your views here.

""" define index view for index route"""
def index(request):
    return render(request,'shortner/index.html')

""" define create view for create shortner urls of urls"""
def create(request):
    if request.method == 'POST': ## check request method is post
        url = request.POST['link'] ## get link of user inputed (from request object)
        uid = str(uuid.uuid4())[:4] ## set uuid

        ## TODO : user = request.user ## get user object for create url shorted
        new_url = Urls(links=url,uuid=uid) ## create new url shorted using Urls class
        new_url.save() ## save url shorted in database
        return HttpResponse(uid) ## return uuid of url shorted in database

""" define for get url shorted and return orginal url"""
def return_orginal_url(request,uuid): 
    orginal_url = Urls.objects.get(uuid=uuid) ## get orginal url using with uuid of url shorted
    return redirect(orginal_url.links)  ## redirect user to page of orginal url
