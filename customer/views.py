from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import Customer, CustomerAddress
from .serializers import CustomerSerializer, CustomerAddressSerializer

import logging
db_logger = logging.getLogger('db')

# Create your views here.


class CustomerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        db_logger.info(request.user.customer_id)
        snippets = Customer.objects.all().filter(is_active=True)
        serializer = CustomerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):

    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


class CustomerAddressView(APIView):
    def get(self, request, format=None):
        snippets = CustomerAddress.objects.all().filter(is_active=True)
        serializer = CustomerAddressSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = CustomerAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerAddressDetailView(APIView):

    def get_object(self, pk):
        try:
            return CustomerAddress.objects.get(pk=pk)
        except CustomerAddress.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerAddressSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CustomerAddressSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)
