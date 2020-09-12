from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def product_list(request):
    # GET list of Product, POST a new Product, DELETE all Product
    if request.method == 'GET':
        product = Product.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            product = product.filter(name__icontains=name)
        
        product_serializer = ProductSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        # product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Product.objects.all().delete()
        return JsonResponse({'message': '{} Categories was/were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    # find product by pk (id)
    try: 
        product = Product.objects.get(pk=pk) 
        if request.method == 'GET': 
            product_serializer = ProductSerializer(product) 
            return JsonResponse(product_serializer.data)
        elif request.method == 'PUT': 
            product_data = JSONParser().parse(request) 
            product_serializer = ProductSerializer(product, data=product_data) 
            if product_serializer.is_valid(): 
                product_serializer.save() 
                return JsonResponse(product_serializer.data) 
            return JsonResponse(product_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            product.delete() 
            return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Product.DoesNotExist: 
        return JsonResponse({'message': 'The Product does not exist'}, status=status.HTTP_404_NOT_FOUND) 

