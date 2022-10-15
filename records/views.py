from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee, Inventory, Report
from .serializers import SerEmployee, SerInventory, SerReport


class VSEmployee(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = SerEmployee


class VSInventory(viewsets.ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = SerInventory


class VSReport(viewsets.ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = SerReport


class EmployeeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'employee_list.html'

    def get(self, request):
        queryset = Employee.objects.all()
        return Response({'profiles': queryset})


def sample(request):
    return render(request, 'employee.html')

# browser <-> viewsets (via urls) <-> serializer <-> models <-> database