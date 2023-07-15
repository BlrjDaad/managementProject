from django.urls import path
from ..accounts.views import *
from ..company.views import *
from ..invitations.views import *


api_urls = [
    path('company', CompanyList.as_view()),
    path('company/<int:pk>', CompanyView.as_view()),
    path('company/<int:company_pk>/departments', DepartmentList.as_view()),
    path('company/<int:company_pk>/departments/<int:pk>', DepartmentView.as_view()),
    path('company/<int:company_pk>/departments/<int:department_pk>/employees', EmployeeList.as_view()),
    path('company/<int:company_pk>/departments/<int:department_pk>/employees/<int:pk>', EmployeeView.as_view()),
    path('company/<int:company_pk>/departments/<int:department_pk>/invitations', InvitationsList.as_view()),
    path('company/<int:company_pk>/departments/<int:department_pk>/invitations/<int:pk>', InvitationView.as_view()),
    path('company/<int:company_pk>/managers', ManagerList.as_view()),
    path('company/<int:company_pk>/managers/<int:pk>', ManagerView.as_view()),
]
