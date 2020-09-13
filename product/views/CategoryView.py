from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser,MultiPartParser,FormParser
from rest_framework import status
 
from product.models import Category
from product.serializers import CategorySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def category_list(request):
    # GET list of Category, POST a new Category, DELETE all Category
    if request.method == 'GET':
        category = Category.objects.all() 
        
        name = request.GET.get('name', None)
        if name is not None:
            category = category.filter(name__icontains=name)
        
        category_serializer = CategorySerializer(category, many=True)
        return JsonResponse(category_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        # parser_classes = (FormParser, MultiPartParser, JSONParser)
        # category_data = MultiPartParser().parse(request)
        category_serializer = CategorySerializer(data=request.data)
        if category_serializer.is_valid():
            category_serializer.save()
            return JsonResponse(category_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Category.objects.all().delete()
        return JsonResponse({'message': '{} Categories was/were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def category_detail(request, pk):
    # find category by pk (id)
    try: 
        category = Category.objects.get(pk=pk) 
        if request.method == 'GET': 
            category_serializer = CategorySerializer(category) 
            return JsonResponse(category_serializer.data)
        elif request.method == 'PUT': 
            category_serializer = CategorySerializer(category, data=request.data) 
            if category_serializer.is_valid(): 
                category_serializer.save() 
                return JsonResponse(category_serializer.data) 
            return JsonResponse(category_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            category.delete() 
            return JsonResponse({'message': 'Category was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist: 
        return JsonResponse({'message': 'The Category does not exist'}, status=status.HTTP_404_NOT_FOUND) 