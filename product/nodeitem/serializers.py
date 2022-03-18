from rest_framework import serializers
from nodeitem.models import Mobile,Laptop,User

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Mobile
        fields=['name','description','processor','ram','screen_size','color']


class LaptopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Laptop
        fields=['name','description','processor','ram','hd_capacity']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']