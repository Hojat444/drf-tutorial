from django.urls import path
from .views import (
    concept_list,
    concept_detail,
    relationship_list,
    relationship_detail,
)

urlpatterns = [
    path('concepts/', concept_list, name='concept-list'),
    path('concepts/<int:pk>/', concept_detail, name='concept-detail'),
    path('relationships/', relationship_list, name='relationship-list'),
    path('relationships/<int:pk>/', relationship_detail, name='relationship-detail'),
]
