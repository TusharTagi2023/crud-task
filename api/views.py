from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
from .serilizers import *
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def function_api(request):
    if request.method == 'GET':
        try:
            json_data=request.body
            if json_data:
                stream=io.BytesIO(json_data)
                pythondata=JSONParser().parse(stream)
                id=pythondata.get('id')
                if pythondata:
                    if id & len(pythondata)<2:
                        data=Data.objects.get(id=id)
                        srz=Dataserializer(data)
                        return JsonResponse(srz.data)
                    msg={'message':'Only share the id'} 
                    return JsonResponse(msg, status=404)                 
                data=Data.objects.all()
                srz=Dataserializer(data, many=True)
                return JsonResponse(srz.data, safe=False)
            return JsonResponse({'message':'Your body is empty'}, status=404)
        except Exception as e:
            msg={'message':str(e)}
            return JsonResponse(msg, status=404)
    elif request.method == 'POST':
        try:
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            srz=Dataserializer(data=pythondata)
            if srz.is_valid():
                srz.save()
                msg={'message':'Your data is save'}
                return JsonResponse(msg)
            msg={'message':'Your data is not in proper format, Please provide proper and formated data'}
            return JsonResponse(msg,status=404)            
        except Exception as e:
            msg={'message':str(e)}
            return JsonResponse(msg, status=404)        
    elif request.method == 'DELETE':
        try:
            json_data=request.body
            data=json.loads(json_data)
            id=data.get('id')
            if id & len(data)<2:
                dlt=Data.objects.get(id=id)
                dlt.delete()
                msg={'message':'given data is deleted'}
                return JsonResponse(msg)
            msg={'message':'Your data is not deleted, you cant provide proper input]'}
            return JsonResponse(msg,status=404)
        except Exception as e:
            msg={'message':str(e)}
            return JsonResponse(msg, status=404)  
    elif request.method == 'PUT':
        try:    
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id=pythondata.get('id')
            stu=Data.objects.get(id=id)
            srz=Dataserializer(stu, data=pythondata, partial=True)
            if srz.is_valid():
                srz.save()
                msg={'msg':'Your data is updated partially'}
                return JsonResponse(msg)
            msg={'msg':'Your data is not update coz u dont provide proper data'}
            return JsonResponse(msg, status=404)
        except Exception as e:
            msg={'message':str(e)}
            return JsonResponse(msg, status=404)
    elif request.method == 'PATCH':
        try:    
            json_data=request.body
            stream=io.BytesIO(json_data)
            pythondata=JSONParser().parse(stream)
            id=pythondata.get('id')
            stu=Data.objects.get(id=id)
            srz=Dataserializer(stu, data=pythondata)
            if srz.is_valid():
                srz.save()
                msg={'msg':'Your data is updated fully'}
                return JsonResponse(msg)
            msg={'msg':'Your data is not update coz you dont provide full and valid data'}
            return JsonResponse(msg, status=404)
        except Exception as e:
            msg={'message':str(e)}
            return JsonResponse(msg, status=404)
        




