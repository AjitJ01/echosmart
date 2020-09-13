from rest_framework import serializers
from user.models import UserType
from user.models import User
from user.models import ActivityHistory


class UserTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserType
        fields = ('id', 'utype', 'description')


class UserSerializer(serializers.ModelSerializer):

    utype_id = serializers.PrimaryKeyRelatedField(queryset=UserType.objects.all(), required=False, allow_null=True, default=None) 

    class Meta:
        model = User
        fields = ('id', 'utype_id', 'title' ,'first_name' ,'last_name' ,'address' ,'pin' ,'email' ,'contact_no' ,'alt_contact_no' ,'password' ,'date_of_bith' ,'proof_id' ,'image', 'created_on', 'last_modified_on')
        extra_kwargs = {'date_of_bith': {'required': False}, 'proof_id': {'required': False},'utype_id': {'required': False}, }

class ActivityHistorySerializer(serializers.ModelSerializer):
        
    class Meta:
        model = ActivityHistory
        fields = ('id', 'activity_by', 'operation', 'entity', 'description', 'time')