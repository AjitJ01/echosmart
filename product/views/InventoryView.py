from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from product.models import Inventory
from product.serializers import InventorySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def inventory_list(request):
    # GET list of Inventory, POST a new Inventory, DELETE all Inventory
    if request.method == 'GET':
        inventory = Inventory.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            inventory = inventory.filter(name__icontains=name)
        
        inventory_serializer = InventorySerializer(inventory, many=True)
        return JsonResponse(inventory_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        inventory_data = JSONParser().parse(request)
        inventory_serializer = InventorySerializer(data=inventory_data)
        if inventory_serializer.is_valid():
            inventory_serializer.save()
            return JsonResponse(inventory_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Inventory.objects.all().delete()
        return JsonResponse({'message': '{} Categories was/were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def inventory_detail(request, pk):
    # find inventory by pk (id)
    try: 
        inventory = Inventory.objects.get(pk=pk) 
        if request.method == 'GET': 
            inventory_serializer = InventorySerializer(inventory) 
            return JsonResponse(inventory_serializer.data)
        elif request.method == 'PUT': 
            inventory_serializer = InventorySerializer(inventory, data=request.data) 
            if inventory_serializer.is_valid(): 
                inventory_serializer.save() 
                return JsonResponse(inventory_serializer.data) 
            return JsonResponse(inventory_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            inventory.delete() 
            return JsonResponse({'message': 'Inventory was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Inventory.DoesNotExist: 
        return JsonResponse({'message': 'The Inventory does not exist'}, status=status.HTTP_404_NOT_FOUND)