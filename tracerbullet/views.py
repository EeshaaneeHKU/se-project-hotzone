import requests
from django.http import JsonResponse
from django.shortcuts import render 
import json 
import urllib.request 
from .forms import UserForm
from .models import UserDetails

def index(request): 
    url = 'https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q='
    city = "HONG KONG CULTURAL CENTRE"

    myUser = UserDetails()
    i=0
    if request.method == 'GET':
        text = request.GET.get('button_text')
        if (text!=None):
            myarr = text.split(" ")
            for i in range (len(myarr)):
                url +="%20"+myarr[i]
            r = requests.get(url.format()).json()
            myUser.name = 'Amy'
            myUser.address = r[0]['nameEN']
            myUser.x_coordinate = r[0]['x']
            myUser.y_coordinate = r[0]['y']
            myUser.save() 
    form = UserForm()

    return render(request, "tracerbullet/index.html")
    