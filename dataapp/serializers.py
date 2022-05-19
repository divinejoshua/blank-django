from rest_framework import serializers
from .models import NameList


#Register a user
class NameListSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameList
        fields = ['name', 'department', 'level']
