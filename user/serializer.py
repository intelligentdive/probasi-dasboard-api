from rest_framework import serializers

from . import services
from rest_framework import serializers
from .models import User,Profileinfo1,Profileinfolocationbd,Profileinfolocationabroad,Profileinfoexperience


class UserCreateSerializerphone(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('fullname', 'phone_number', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Create a user with the provided data
        user = User.objects.create_user(**validated_data)
        return user
    


class UserCreateSerializeremail(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('fullname', 'email', 'password')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        # Create a user with the provided data
        user = User.objects.create_user(**validated_data)
        return user   



class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    fullname = serializers.CharField()
   
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        return services.UserDataClass(**data)
    

class ProfileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profileinfo1
        fields = ('user_name', 'gender', 'date_of_birth')  # Include only the fields that users can provide when creating a profile


class Profileloactionbd(serializers.ModelSerializer):
    class Meta:
        model = Profileinfolocationbd
        fields = ('District',)



class Profileloactionabroad(serializers.ModelSerializer):
    class Meta:
        model = Profileinfolocationabroad
        fields = ('countryname','city','duration')   







class Profileinfoexperienceserializer(serializers.ModelSerializer):
    class Meta:
        model = Profileinfoexperience
        fields = ('durationstay','industry','areaofexpertise','durationstay')  

