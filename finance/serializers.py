from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['id' , 'name' , 'owner']
        
    def validate_name(self,name):
        if not name.strip() :
            raise serializers.ValidationError("Category name cannot be empty or spaces.")  
        return name