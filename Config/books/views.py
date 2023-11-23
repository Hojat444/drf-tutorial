from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveUpdateDestroyAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from books.models import Book
from .serializer import BookListSerializer,BookDetailSerializer,UserSerializer
from .permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from django.db import connection

# Create your views here.

# class BookList(ListCreateAPIView):
#     #permission_classes = (IsAuthenticatedOrReadOnly,)
#     authentication_classes = (TokenAuthentication,)
#     queryset = Book.objects.all()
#     serializer_class = BookListSerializer
    
    
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     #permission_classes = (IsAuthenticatedOrReadOnly,)
    
#    # permission_classes = (IsOwnerOrReadOnly,)
#     queryset = Book.objects.all()
#     serializer_class = BookDetailSerializer    
    

# class UserList(ListAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
    
# class UserDetail(RetrieveAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer    
    
    
class BookViewSet(viewsets.ModelViewSet):
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Book.objects.all()
    serializer_class = BookListSerializer
    
    
class UserViewSet(viewsets.ModelViewSet):
    #http_method_names = ['get']
    
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    

    
        
    