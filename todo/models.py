from django.db import models

class TodoItem(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('WORKING', 'Working'),
        ('PENDING_REVIEW', 'Pending Review'),
        ('COMPLETED', 'Completed'),
        ('OVERDUE', 'Overdue'),
        ('CANCELLED', 'Cancelled'),
    ]

    timestamp = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    due_date = models.DateField(null=True, blank=True)
    tags = models.CharField(max_length=100, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='OPEN')

    def save(self, *args, **kwargs):
        if self.due_date and self.due_date < self.timestamp.date():
            raise ValueError("Due date cannot be before the creation timestamp")
        super().save(*args, **kwargs)
