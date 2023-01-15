from django.urls import path
from .views import Register,List
urlpatterns = [
    path('', Register.as_view(),name = 'register'),
    path('list', List.as_view(),name = 'list'),
    path('list/<int:roll_no>', List.as_view(),name = 'list-search'),
]
