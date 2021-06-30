from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EmployeeSerializer
from .models import Employee

# Create your views here.
@api_view(["GET"])
def apiOverview(request):
    api_urls={
        "list":"/emp-list/",
        "create": "/emp-create/",
        "Detail-view":"/emp-detail/<str:pk>/",
        "Update": "/emp-update/<str:pk>/",
        "Delete": "/emp-delete/<str:pk>/",
    }
    return Response(api_urls)
@api_view(["GET"])
def employee(request):
    employee=Employee.objects.all()
    serializer=EmployeeSerializer(employee, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def employee_detail(request,pk):
    employee=Employee.objects.get(id=pk)
    serializer=EmployeeSerializer(employee, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def create(request):
    serializer=EmployeeSerializer(request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def update(request, pk):
    employee = Employee.objects.get(id=pk)
    serializer  =EmployeeSerializer(instance=employee, data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def delete(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    return Response("deleted successfully")
