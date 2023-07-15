from django.shortcuts import render
from .models import Employee, Manager
from .serializer import EmployeeSerializer, ManagerSerializer
from ..company.models import Department, Company
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class EmployeeList(APIView):
    """
    List all users, or create a new user.
    """

    def get(self, request, company_pk, department_pk, format=None):
        snippets = Employee.objects.filter(department_id=department_pk)
        serializer = EmployeeSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, company_pk, department_pk, format=None):
        department = get_object_or_404(Department, pk=department_pk)
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(department=department)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeView(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, company_pk, department_pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EmployeeSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save(role=3)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ManagerList(APIView):
    """
    List all users, or create a new user.
    """

    def get(self, request, company_pk, format=None):
        snippets = Manager.objects.filter(company_id=company_pk)
        serializer = ManagerSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, company_pk, format=None):
        company = get_object_or_404(Company, pk=company_pk)
        serializer = ManagerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(company=company, role=2, subrole=2)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerView(APIView):
    """
    Retrieve, update or delete a user instance.
    """
    def get_object(self, pk):
        try:
            return Manager.objects.get(pk=pk)
        except Manager.DoesNotExist:
            raise Http404

    def get(self, request, pk, company_pk, department_pk, format=None):
        manager = self.get_object(pk)
        serializer = ManagerSerializer(emplomanageryee)
        return Response(serializer.data)

    def put(self, request, pk, company_pk, department_pk, format=None):
        snippet = self.get_object(pk)
        serializer = ManagerSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save(role=2)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
