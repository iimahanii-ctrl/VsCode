from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    student_type = models.CharField(max_length=50, choices=[
        ('child', 'Child (4-12)'),
        ('teen', 'Teen (13-17)'),
        ('adult', 'Adult (18+)')
    ])
    preferred_day = models.CharField(max_length=20)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.created_at}"