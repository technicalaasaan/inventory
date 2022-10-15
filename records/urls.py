from rest_framework import routers

from .views import VSEmployee, VSReport, VSInventory, EmployeeList

inv_app = routers.DefaultRouter()

inv_app.register('employee', VSEmployee)
inv_app.register('inventory', VSInventory)
inv_app.register('report', VSReport)
