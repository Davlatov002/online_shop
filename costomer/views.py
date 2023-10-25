from .models import Costomer, Shopcard
from .serialazers import Costomerserializers, Shopcardserializers, UpdateCostomerserialazer, UpdateShopcardserialazer
from rest_framework.decorators import api_view
from rest_framework import status, serializers
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def all_purchases(request, pk):
    if request.method == 'GET':
        shopcard = Shopcard.objects.all()
        castomor = Costomer.objects.get(id=pk)
        filtered = [x for x in shopcard if x.owner.id == castomor.id]
        data = Shopcardserializers(filtered, many=True) 
        return Response(data.data)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def the_purchase_price(request, pk):
    if request.method == 'GET':
        shopcard = Shopcard.objects.all()
        castomor = Costomer.objects.get(id=pk)
        filtered = [x for x in shopcard if x.owner.id == castomor.id]
        pric = 0
        i:Shopcard
        for i in filtered:
            pric += i.get_total_price()
        if pric > 1000000:
            data = {"Butun harit":f"1 000 000 so'mdan oshgan va {pric} so'mni tashkil qiladi"}
            return Response(data)
        else:
            data = {"Butun harit":f"1 000 000 so'mdan kam va {pric} so'mni tashkil qiladi"}
            return Response(data)


@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def costomer(request):
    if request.method == 'GET':
        costomer = Costomer.objects.all()
        serializer = Costomerserializers(costomer, many=True)
        return Response(serializer.data)  

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def costomer_id(request, pk):
    if request.method == 'GET':
        costomer = Costomer.objects.get(id=pk)        
        serializer = Costomerserializers(costomer)
        return Response(serializer.data)    

@swagger_auto_schema(method='POST', request_body=Costomerserializers, operation_description="Malumotlarni kirting")             
@api_view(['POST'])
def costomer_created(request):
    costomer = Costomerserializers(data=request.data)
    if Costomer.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
    if costomer.is_valid():
        costomer.save()   
        return Response(costomer.data)       
    else:                      
        return Response(status=status.HTTP_404_NOT_FOUND)   
    
@swagger_auto_schema(method='PATCH', request_body=UpdateCostomerserialazer, operation_description="Yangilamaoqchi bo'lgan costumirning ID sini kirting")
@api_view(['PATCH'])
def costomer_update(request, pk):
    costomer = Costomer.objects.get(id=pk)        
    data = Costomerserializers(instance=costomer, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='DELETE',operation_description="O'chirmoqchi bo'lgan Costomerning ID ni kirting")
@api_view(['DELETE'])
def costomer_delete(request, pk):
    if request.method == 'DELETE':
        costomer = Costomer.objects.get(id=pk)
        costomer.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def shopcard(request):
    if request.method == 'GET':
        shopcardd = Shopcard.objects.all()
        serializer = Shopcardserializers(shopcardd, many=True)
        return Response(serializer.data)
    
@swagger_auto_schema(methods='GET')
@api_view(['GET'])
def shopcard_id(request, pk):
    if request.method == 'GET':
        shopc = Shopcard.objects.get(id=pk)        
        serializer = Shopcardserializers(shopc)
        return Response(serializer.data)  
  
@swagger_auto_schema(method='POST', request_body=Shopcardserializers, operation_description="Malumotlarni kirting") 
@api_view(['POST'])
def shopcard_created(request):
    if request.method == 'POST':
        shopcard = Shopcardserializers(data=request.data)
        if shopcard.is_valid():
            shopcard.save()
            return Response(shopcard.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

@swagger_auto_schema(method='PATCH', request_body=UpdateShopcardserialazer, operation_description="Yangilamaoqchi bo'lgan Shopcardning ID sini kirting")
@api_view(['PATCH'])
def shopcard_update(request, pk):
    shopcard = Shopcard.objects.get(id=pk)        
    data = Shopcardserializers(instance=shopcard, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@swagger_auto_schema(method='DELETE',operation_description="O'chirmoqchi bo'lgan shopcardning ID ni kirting")
@api_view(['DELETE'])
def shopcard_delete(request, pk):
    if request.method == 'DELETE':
        shopcard = Shopcard.objects.get(id=pk)
        shopcard.delete()
        return Response(status=status.HTTP_202_ACCEPTED)