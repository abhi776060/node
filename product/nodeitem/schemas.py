

from rest_framework import serializers
from nodeitem.models import Mobile,Laptop




class ItemSchemasSerializer(serializers.ModelSerializer):
    
     class Meta:
        model=Mobile
        fields=['name','description','processor','ram','screen_size','color']

