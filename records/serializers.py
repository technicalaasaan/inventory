from rest_framework import serializers
from .models import Employee, Inventory, Report


class SerEmployee(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"


class SerInventory(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class SerReport(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = "__all__"
