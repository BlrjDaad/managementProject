from django.shortcuts import render
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import *
from .serializer import *


# Create your views here.
class InvitationsList(APIView):
    """
    List all invitation, or create a new company.
    """

    def get(self, request, company_pk, department_pk, format=None):

        snippets = EmployeeInvitation.objects.filter(department__id=department_pk)
        serializer = EmployeeInvitationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, company_pk, department_pk, format=None):
        serializer_info = InvitationInfoSerializer(data=request.data.get("invitation_info"))
        email = request.data.get("invitation_info").get('email')
        serializer_invi = EmployeeInvitationSerializer(data=request.data)
        if serializer_info.is_valid() and serializer_invi.is_valid():
            org = Department.objects.filter(id=department_pk).first()
            serializer_info.save()
            invitation_info = InvitationInfo.objects.filter(email=email).first()
            serializer_invi.save(department=org, invitation_info=invitation_info)
            return Response(serializer_invi.data, status=status.HTTP_201_CREATED)
        return Response(serializer_invi.errors, status=status.HTTP_400_BAD_REQUEST)


class InvitationView(APIView):
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