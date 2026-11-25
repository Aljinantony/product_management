from rest_framework import serializers
from django.contrib.auth.models import User
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=product

        fields=[
            'id',
            'product_name',
            'product_code',
            'cateogery',
            'price',
            'stock_quantity'

        ]
class UserRegistrationSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,min_length=8)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password'
        ]
    def create(self,validated_data):
        user=User.objects.create_user(username=validated_data['username'],
        email=validated_data['email'],
        password=validated_data['password'])

        return user