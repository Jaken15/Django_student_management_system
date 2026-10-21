from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100,null=True, blank=True)
    student_name = models.CharField(max_length=100)
    student_subject = models.CharField(max_length=100)
    student_profile = models.ImageField(upload_to='profile_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.student_name} - {self.student_subject}"
