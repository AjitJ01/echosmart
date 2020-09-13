from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from user.models import User
from user.serializers import UserSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    # GET list of User, POST a new User, DELETE all User
    if request.method == 'GET':
        user = User.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            user = user.filter(name__icontains=name)
        
        user_serializer = UserSerializer(user, many=True)
        return JsonResponse(user_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        # user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} User was/were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, pk):
    # find user by pk (id)
    try: 
        user = User.objects.get(pk=pk) 
        if request.method == 'GET': 
            user_serializer = UserSerializer(user) 
            return JsonResponse(user_serializer.data)
        elif request.method == 'PUT': 
            user_serializer = UserSerializer(user, data=request.data) 
            if user_serializer.is_valid(): 
                user_serializer.save() 
                return JsonResponse(user_serializer.data) 
            return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            user.delete() 
            return JsonResponse({'message': 'User was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The User does not exist'}, status=status.HTTP_404_NOT_FOUND)