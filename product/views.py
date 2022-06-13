from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ProductMaster
from .serializers import ProductMasterSerializer
from .models import GroupMaster
from .serializers import GroupMasterSerializer
from .models import ProductCategory
from .serializers import ProductCategorySerializer


# Create your views here.


class ProductMasterView(APIView):
    def get(self, request, format=None):
        snippets = ProductMaster.objects.all().filter(is_active=True)
        serializer = ProductMasterSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductMasterDetailView(APIView):

    def get_object(self, pk):
        try:
            return ProductMaster.objects.get(pk=pk)
        except ProductMaster.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductMasterSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductMasterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


class GroupMasterView(APIView):
    def get(self, request, format=None):
        snippets = GroupMaster.objects.all().filter(is_active=True)
        serializer = GroupMasterSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GroupMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GroupMasterDetailView(APIView):

    def get_object(self, pk):
        try:
            return GroupMaster.objects.get(pk=pk)
        except GroupMaster.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GroupMasterSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = GroupMasterSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


class ProductCategoryView(APIView):
    def get(self, request, format=None):
        snippets = ProductCategory.objects.all().filter(is_active=True)
        serializer = ProductCategorySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductCategoryDetailView(APIView):

    def get_object(self, pk):
        try:
            return ProductCategory.objects.get(pk=pk)
        except ProductCategory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductCategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = ProductCategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)
