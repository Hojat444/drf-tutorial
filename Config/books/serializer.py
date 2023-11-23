from rest_framework import serializers
from books.models import Book,Writer
from django.contrib.auth.models import User


class WriterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Writer
        fields = ("first_name","last_name")



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = "__all__"



class BookListSerializer(serializers.ModelSerializer):
    owner = UserSerializer(many=False)
    writers = WriterSerializer(many=True)
    class Meta:
        model = Book
        fields = ("id","title","owner","writers")
        
        
   
class BookDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ("title","author","code")        
    