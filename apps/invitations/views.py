
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from ..questionnaire.models import Questionnaire
from ..accounts.models import Employee
from .serializer import *


# Create your views here.
class InvitationsList(APIView):
    """
    List all invitation, or create a new company.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, company_pk, department_pk, format=None):

        snippets = EmployeeInvitation.objects.filter(department__id=department_pk)
        serializer = EmployeeInvitationSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, company_pk, department_pk, format=None):
        invitations_infos = request.data.get("invitations_infos")
        del request.data["invitations_infos"]
        serializer_invi = EmployeeInvitationSerializer(data=request.data)
        if serializer_invi.is_valid():
            org = Department.objects.filter(id=department_pk).first()
            invitation_obj = serializer_invi.save(department=org)
            for invitation_info in invitations_infos:
                serializer_info = InvitationInfoSerializer(data=invitation_info)
                if serializer_info.is_valid():
                    employee = Employee.objects.filter(email=invitation_info.get('email')).first()

                    if employee:
                        questionnaire = Questionnaire.objects.create(invitation=invitation_obj, employee=employee)
                    else:
                        questionnaire = Questionnaire.objects.create(invitation=invitation_obj)
                    serializer_info.save(invitation=invitation_obj)

            return Response(serializer_invi.data, status=status.HTTP_201_CREATED)
        return Response(serializer_invi.errors, status=status.HTTP_400_BAD_REQUEST)


class InvitationsInfosList(APIView):
    """
    List all invitation, or create a new company.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, company_pk, department_pk, invitation_pk, format=None):

        snippets = InvitationInfo.objects.filter(invitation__pk=invitation_pk)
        serializer = InvitationInfoSerializer(snippets, many=True)
        return Response(serializer.data)


class InvitationView(APIView):
    """
    Retrieve, update or delete a company instance.
    """

    serializer_class = EmployeeInvitationSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, company_pk, department_pk, pk, format=None):
        snippets = EmployeeInvitation.objects.filter(pk=pk)
        serializer = EmployeeInvitationSerializer(snippets, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = EmployeeInvitationSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)