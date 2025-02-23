from django.db import models

# Create your models here.
from django.db import models

class Complaint(models.Model):
    PRIORITY_CHOICES = [
        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.CharField(max_length=100)
    issue_description = models.TextField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.product} - {self.status}"