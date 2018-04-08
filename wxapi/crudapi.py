from wxapi.models import UserInfo, Merchants, Job, SignUp
from wxapi.serializers import UserInfoSerializer,MerchantsSerializer,JobSerializer,SignUpSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
@csrf_exempt
def snippet_list(request,model,formatting):
    if request.method == 'GET':
        snippets = eval(model).objects.all()
        serializer = eval(formatting)(snippets, many=True)  #查询到job数据
        #循环查询用户数据
        Merchantarry  =  []
        for i in snippets:
            Merchant = i.user_id.merchants.filter(user_id_id = i.user_id)         #关联查询
            Merchantarry.append(MerchantsSerializer(Merchant, many=True).data)   #序列化
        serializerData =serializer.data
        for i in serializerData:  #塞数据
            i['Merchant'] = Merchantarry[serializerData.index(i)][0]['name']
            i['MerchantId'] = Merchantarry[serializerData.index(i)][0]['id']
        return serializer.data


    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = formatting(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request,model,formatting, pk):
    try:
        snippet = eval(model).objects.get(pk = pk)
    except eval(model).DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = eval(formatting)(snippet)
        return serializer.data

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = eval(formatting)(snippet, data=data)
        print('==================')
        if serializer.is_valid():
            serializer.save()
            print(data)
            return serializer.data
        return serializer.errors

    elif request.method == 'DELETE':
        print('-----------------')
        snippet.delete()
        return HttpResponse(status=204)