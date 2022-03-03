from django.shortcuts import render
from rest_framework.parsers import JSONParser
# allows other domains to acces our api methods
# (our front-end project)
from django.views.decorators.csrf import csrf_exempt
from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer
from fjango.http.response import JsonResponse

# Create your views here.
@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method == 'POST':
        # using JSONParser for input
        department_data = JSONParser().parse(request)
