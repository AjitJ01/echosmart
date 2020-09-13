from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from user.models import UserType
from user.serializers import UserTypeSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def user_type_list(request):
    # GET list of User Type, POST a new User Type, DELETE all User Types
    if request.method == 'GET':
        user_type = UserType.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            user_type = user_type.filter(name__icontains=name)
        
        user_type_serializer = UserTypeSerializer(user_type, many=True)
        return JsonResponse(user_type_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        # user_type_data = JSONParser().parse(request)
        user_type_serializer = UserTypeSerializer(data=request.data)
        if user_type_serializer.is_valid():
            user_type_serializer.save()
            return JsonResponse(user_type_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = UserType.objects.all().delete()
        return JsonResponse({'message': '{} User Type was/were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_type_detail(request, pk):
    # find user_type by pk (id)
    try: 
        user_type = UserType.objects.get(pk=pk) 
        if request.method == 'GET': 
            user_type_serializer = UserTypeSerializer(user_type) 
            return JsonResponse(user_type_serializer.data)
        elif request.method == 'PUT': 
            user_type_serializer = UserTypeSerializer(user_type, data=request.data) 
            if user_type_serializer.is_valid(): 
                user_type_serializer.save() 
                return JsonResponse(user_type_serializer.data) 
            return JsonResponse(user_type_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            user_type.delete() 
            return JsonResponse({'message': 'User Type was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except UserType.DoesNotExist: 
        return JsonResponse({'message': 'The User Type does not exist'}, status=status.HTTP_404_NOT_FOUND) 
