from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from user.models import ActivityHistory
from user.serializers import ActivityHistorySerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def activity_list(request):
    # GET list of ActivityHistory, POST a new ActivityHistory, DELETE all ActivityHistory
    if request.method == 'GET':
        activity = ActivityHistory.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            activity = activity.filter(name__icontains=name)
        
        activity_serializer = ActivityHistorySerializer(activity, many=True)
        return JsonResponse(activity_serializer.data, safe=False)
        
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        activity_serializer = ActivityHistorySerializer(data=request.data)
        if activity_serializer.is_valid():
            activity_serializer.save()
            return JsonResponse(activity_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(activity_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = ActivityHistory.objects.all().delete()
        return JsonResponse({'message': '{} Activities was/were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
@api_view(['GET', 'PUT', 'DELETE'])
def activity_detail(request, pk):
    # find activity by pk (id)
    try: 
        activity = ActivityHistory.objects.get(pk=pk) 
        if request.method == 'GET': 
            activity_serializer = ActivityHistorySerializer(activity) 
            return JsonResponse(activity_serializer.data)
        elif request.method == 'PUT': 
            activity_data = JSONParser().parse(request) 
            activity_serializer = ActivityHistorySerializer(activity, data=activity_data) 
            if activity_serializer.is_valid(): 
                activity_serializer.save() 
                return JsonResponse(activity_serializer.data) 
            return JsonResponse(activity_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
        elif request.method == 'DELETE': 
            activity.delete() 
            return JsonResponse({'message': 'ActivityHistory was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except ActivityHistory.DoesNotExist: 
        return JsonResponse({'message': 'The ActivityHistory does not exist'}, status=status.HTTP_404_NOT_FOUND) 

