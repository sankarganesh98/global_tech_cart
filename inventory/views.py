from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import Inventory
from .serializers import InventorySerializer


# Create your views here.


class InventoryView(APIView):
    def get(self, request, format=None):
        snippets = Inventory.objects.all().filter(is_active=True)
        serializer = InventorySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryDetailView(APIView):

    def get_object(self, pk):
        try:
            return Inventory.objects.get(pk=pk)
        except Inventory.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = InventorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = InventorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)
