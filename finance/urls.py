from django.urls import path

from . import views

app_name = 'finance'

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='categoriesList'),
]