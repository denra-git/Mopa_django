from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Category
from .serializers import CategorySerializer

from rest_framework.permissions import IsAuthenticated


class CategoryListView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        categories = Category.objects.filter(owner=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)