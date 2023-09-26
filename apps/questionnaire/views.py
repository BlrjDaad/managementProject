from .serializer import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class QuestionnaireList(APIView):
    """
    List all questionnaires related to a employee , or create a new questionnaire.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, company_pk, department_pk, employee_pk):
        employee = get_object_or_404(Employee, pk=employee_pk)
        print("employee")
        print(employee)
        snippets = Questionnaire.objects.filter(employee__id=employee.pk)
        print("snippets")
        print(snippets)
        serializer = QuestionnaireSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, company_pk, department_pk, employee_pk, format=None):
        serializer = QuestionnaireSerializer(data=request.data)
        if serializer.is_valid():
            org = Employee.objects.filter(id=Employee).first()
            serializer.save(employee=org)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionnaireView(APIView):
    """
    Retrieve, update or delete a department instance.
    """
    permission_classes = [IsAuthenticated]

    def get_object(self, company_pk, department_pk, employee_pk, pk):
        try:
            return Questionnaire.objects.get(pk=pk)
        except Questionnaire.DoesNotExist:
            raise Http404

    def get(self, request, company_pk, department_pk, employee_pk, pk,  format=None):
        snippet = self.get_object(company_pk, department_pk, employee_pk, pk)
        serializer = QuestionnaireSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, company_pk, department_pk, employee_pk, pk, format=None):
        snippet = self.get_object(company_pk, department_pk, employee_pk, pk)
        serializer = QuestionnaireSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_pk, department_pk, employee_pk, pk, format=None):
        snippet = self.get_object(company_pk, department_pk, employee_pk, pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)