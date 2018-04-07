from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from wxapi.models import UserInfo, Merchants, Job, SignUp
from django.contrib.auth.models import User
from wxapi.serializers import UserInfoSerializer,MerchantsSerializer,JobSerializer,SignUpSerializer
from wxapi.crudapi import *
# Create your views here.
from django.core import serializers

def rdata(request):
    model = request.GET['table']
    formatting = request.GET['tableClass']
    pk = request.GET['data']
    data = snippet_detail(request, model, formatting, pk)
    return JsonResponse(data, safe=False)


def homelist(request):
    model = request.GET['table']
    formatting = request.GET['tableClass']
    data = snippet_list(request, model, formatting)

    return JsonResponse(data, safe=False)

