from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from .models import Enterprise, EnterpriseAddress, Warehouse, WarehouseAddress
from .serializers import EnterpriseSerializer, EnterpriseAddressSerializer, WarehouseSerializer, WarehouseAddressSerializer



import logging
db_logger = logging.getLogger('db')

# Create your views here.


class EnterpriseView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        db_logger.info(request.user.enterprise_id)
        snippets = Enterprise.objects.all().filter(is_active=True)
        serializer = EnterpriseSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = EnterpriseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnterpriseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Enterprise.objects.get(pk=pk)
        except Enterprise.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnterpriseSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnterpriseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


class EnterpriseAddressView(APIView):
    def get(self, request, format=None):
        snippets = EnterpriseAddress.objects.all().filter(is_active=True)
        serializer = EnterpriseAddressSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = EnterpriseAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EnterpriseAddressDetailView(APIView):

    def get_object(self, pk):
        try:
            return EnterpriseAddress.objects.get(pk=pk)
        except EnterpriseAddress.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnterpriseAddressSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EnterpriseAddressSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


class WarehouseView(APIView):
    def get(self, request, format=None):
        snippets = Warehouse.objects.all().filter(is_active=True)
        serializer = WarehouseSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = WarehouseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseDetailView(APIView):

    def get_object(self, pk):
        try:
            return Warehouse.objects.get(pk=pk)
        except Warehouse.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WarehouseSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WarehouseSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


class WarehouseAddressView(APIView):
    def get(self, request, format=None):
        snippets = WarehouseAddress.objects.all().filter(is_active=True)
        serializer = WarehouseAddressSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # db_logger.info(request.data)
        serializer = WarehouseAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WarehouseAddressDetailView(APIView):

    def get_object(self, pk):
        try:
            return WarehouseAddress.objects.get(pk=pk)
        except WarehouseAddress.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WarehouseAddressSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = WarehouseAddressSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.is_active = 0
        snippet.save()
        return Response("Deleted Successfully", status=status.HTTP_200_OK)


# class EnterpriseUser(APIView):

#     def post(self, request, format=None):
#         enterprise_data = {
#             'company_name': request.data['company_name'],
#             'phone_number': request.data['phone_number'],
#             'email_id': request.data['company_email'],
#             'proprietor_name': request.data['proprietor_name'],
#             'proprietor_email': request.data['proprietor_email'],
#             'enterprise_branch_id': request.data['enterprise_branch_id'],
#             'created_by': request.data['created_by'],
#             'modified_by': request.data['modified_by'],
#         }
#         enterprise_serializer = EnterpriseSerializer(data=enterprise_data)
#         if enterprise_serializer.is_valid():
#             enterprise_serializer.save()
#             enterpriseId = enterprise_serializer.data['enterprise_id']
#             user_data = {
#                 'enterprise': enterpriseId,
#                 'email': request.data['proprietor_email'],
#                 'first_name': request.data['proprietor_name'],
#                 'password': request.data['password'],
#             }
#             user_serializer = RegisterSuperUserSerializer(data=user_data)
#             if user_serializer.is_valid():
#                 user_serializer.save()
#                 return Response({'enterprise': enterprise_serializer.data, 'user': user_serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(enterprise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
