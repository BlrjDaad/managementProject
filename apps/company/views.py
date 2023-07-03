from .serializer import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.
class CompanyList(APIView):
    """
    List all company, or create a new company.
    """

    def get(self, request, format=None):
        snippets = Company.objects.all()
        serializer = CompanySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CompanySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CompanySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DepartmentList(APIView):
    """
    List all departments, or create a new department.
    """

    def get(self, request, company_pk):
        company = get_object_or_404(Company, pk=company_pk)
        snippets = Department.objects.filter(company_id=company.pk)
        serializer = DepartmentSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, company_pk, format=None):
        print("========================")
        print(self.kwargs)
        print(company_pk)
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            org = Company.objects.filter(id=company_pk).first()
            serializer.save(company=org)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DepartmentDetail(APIView):
    """
    Retrieve, update or delete a department instance.
    """
    def get_object(self, pk):
        try:
            return Department.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DepartmentSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = DepartmentSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)