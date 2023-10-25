from .models import Category, Praduct
from .serialazer import Categoriyserializers, Praductserializers, UpdateCategoriyserialazer, UpdatePraductserialazer
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from datetime import date
from costomer.models import Shopcard


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def expired(request):
    if request.method == 'GET':
        praducts = Praduct.objects.all()
        filtered = [x for x in praducts if x.end_data != None and date.today() > x.end_data]
        serializer = Praductserializers(filtered, many=True)
        return Response(serializer.data)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def shop_sell_total(request):
    if request.method == 'GET':
        praducts = Praduct.objects.all()
        ums = 0
        for praduct in praducts:
            ums += praduct.price
        serializer = {'shop_sell_total':ums}
        return Response(serializer)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def best_selling_product(request):
    if request.method == 'GET':
        pradukt = Shopcard.objects.all()
        s = [x.praduct.all() for x in pradukt]
        filtered = max(set(s), key = s.count)
        serializers = Praductserializers(filtered, many=True)
        return Response(serializers.data)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categoriy(request):
    if request.method == 'GET':
        catgoriy = Category.objects.all()
        serializer = Categoriyserializers(catgoriy, many=True)
        return Response(serializer.data) 

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def categoriy_id(request, pk):
    if request.method == 'GET':
        catgoriy = Category.objects.get(id=pk)        
        serializer = Categoriyserializers(catgoriy)
        return Response(serializer.data)    


@swagger_auto_schema(method='POST', request_body=Categoriyserializers, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def categoriy_created(request):
    catgoriy = Categoriyserializers(data=request.data)
    if Category.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if catgoriy.is_valid():
        catgoriy.save()   
        return Response(catgoriy.data)       
    else:                      
        return Response(status=status.HTTP_404_NOT_FOUND)   
    

@swagger_auto_schema(method='PATCH', request_body=UpdateCategoriyserialazer, operation_description="Yangilamaoqchi bo'lgan Categoriyaning ID sini kirting")
@api_view(['PATCH'])
def categoriy_update(request, pk):
    item = Category.objects.get(id=pk)        
    data = Categoriyserializers(instance=item, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='DELETE',operation_description="O'chirmoqchi bo'lgan catigoriyning ID ni kirting")
@api_view(['DELETE'])
def categoriy_delete(request, pk):
    if request.method == 'DELETE':
        categoriy = Category.objects.get(id=pk)
        categoriy.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def praduct(request):
    if request.method == 'GET':
        praduct = Praduct.objects.all()
        serializer = Praductserializers(praduct, many=True)
        return Response(serializer.data)  
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def praduct_id(request, pk):
    if request.method == 'GET':
        praduc = Praduct.objects.get(id=pk)        
        serializer = Praductserializers(praduc)
        return Response(serializer.data) 

@swagger_auto_schema(method='POST', request_body=Praductserializers, operation_description="Malumotlarni kirting")
@api_view(['POST'])
def praduct_created(request):
    praduct = Praductserializers(data=request.data)
    if Praduct.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if praduct.is_valid():
        praduct.save()   
        return Response(praduct.data)       
    else:                      
        return Response(status=status.HTTP_404_NOT_FOUND)   
    

@swagger_auto_schema(method='PATCH', request_body=UpdatePraductserialazer, operation_description="Yangilamaoqchi bo'lgan pradukniing ID sini kirting")
@api_view(['PATCH'])
def praduct_update(request, pk):
    praduct = Praduct.objects.get(id=pk)        
    data = Praductserializers(instance=praduct, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@swagger_auto_schema(method='DELETE',operation_description="O'chirmoqchi bo'lgan Praducningning ID ni kirting")
@api_view(['DELETE'])
def praduct_delete(request, pk):
    if request.method == 'DELETE':
        praduct = Praduct.objects.get(id=pk)
        praduct.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
