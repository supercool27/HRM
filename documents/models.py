from django.db import models
from employee.models import Employee

class Document(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    document_type = models.CharField(max_length=100)  # e.g., Aadhaar, PAN, Resume
    upload = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.document_type} - {self.employee}"
