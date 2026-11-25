from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import product
from.Serializers import(ProductSerializer,UserRegistrationSerializer)


# Create your views here.
#products list and create 
class ProductListCreateAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        products=product.objects.all()
        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)

    #create new product
    def post(self,request):
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    #product retrive update and delete
class productdetailApiview(APIView):
    permission_classes=[IsAuthenticated]
    #get product using id

    def get(self,request,Pk):
        product=get_object_or_404(product,pk=Pk)

        serializer=ProductSerializer(product)
        return Response(serializer.data)
    #update product
    def put(self, request, pk):

        product = get_object_or_404(

            product,

            pk=pk

        )

        serializer = ProductSerializer(

            product,

            data=request.data

        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST

        )
    # Partial update

    def patch(self, request, pk):

        product = get_object_or_404(

            product,

            pk=pk

        )

        serializer = ProductSerializer(

            product,

            data=request.data,

            partial=True

        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST

        )

    # Delete product
    def delete(self, request, pk):

        product = get_object_or_404(

            product,

            pk=pk

        )

        product.delete()

        return Response(

            {"message": "Product deleted successfully"},

            status=status.HTTP_204_NO_CONTENT

        )

# 3. User Registration API

class UserRegistrationAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = UserRegistrationSerializer(

            data=request.data

        )

        if serializer.is_valid():

            serializer.save()

            return Response(

                {"message": "User registered successfully"},

                status=status.HTTP_201_CREATED

            )

        return Response(

            serializer.errors,

            status=status.HTTP_400_BAD_REQUEST

        )