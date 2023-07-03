from django.urls import path
from ..accounts.views import *
from ..company.views import *


api_urls = [
    path('employees', EmployeeList.as_view()),
    path('employee/<int:pk>', EmployeeDetail.as_view()),
    path('company', CompanyList.as_view()),
    path('company/<int:pk>', CompanyDetail.as_view()),
    path('company/<int:company_pk>/departments', DepartmentList.as_view()),
    path('company/<int:company_pk>/department/<int:pk>', DepartmentDetail.as_view()),
]
