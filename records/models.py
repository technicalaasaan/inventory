from django.db import models
from datetime import date

# Create your models here.
class Employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    doj = models.DateField(default=date.today)
    address = models.TextField()
    mobile = models.CharField(max_length=15)

    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.emp_name

    def __repr__(self):
        return self.__str__()


class Inventory(models.Model):
    inv_id = models.AutoField(primary_key=True)
    prod_name = models.CharField(max_length=100)
    serial_no = models.IntegerField()
    mac_id = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, choices=(('chennai', 'CHENNAI'), ('bangalore', 'BANGALORE')), default='chennai')
    doi = models.DateField(default=date.today)
    # email = models.EmailField()

    class Meta:
        db_table = "inventory"

    def __str__(self):
        return self.prod_name

    def __repr__(self):
        return self.__str__()


class Report(models.Model):
    report_id = models.AutoField(primary_key=True)
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(null=True)

    class Meta:
        db_table = "report"

    def __str__(self):
        return f"{self.employee.emp_name} - {self.inventory.prod_name}"

    def __repr__(self):
        return self.__str__()
