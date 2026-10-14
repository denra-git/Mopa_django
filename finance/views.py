from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Category
from .serializers import CategorySerializer


class CategoryListView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        categories = Category.objects.filter(owner=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data=request.data )
        serializer.is_valid(raise_exception=True)
        serializer.save(owner=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self,request,pk):
        category = get_object_or_404(Category,pk=pk,owner=request.user)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    def patch(self,request,pk):
        category = get_object_or_404(Category,pk=pk,owner=request.user)
        serializer = CategorySerializer(category,data=request.data,partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,pk):
        category = get_object_or_404(Category,pk=pk,owner=request.user)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)