from django.db import models
 

class Student(models.Model):
    INTEREST_CHOICES = [
        ('AI', 'Artificial Intelligence'),
        ('ML', 'Machine Learning'),
        ('WD', 'Web Development'),
        ('DS', 'Data Science'),
    ]

    SPECIALIZATION_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('EC', 'Electronics'),
    ]

    RESIDENCE_CHOICES = [
        ('Hostel', 'Hostel'),
        ('Day Scholar', 'Day Scholar'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    interest = models.CharField(max_length=50, choices=INTEREST_CHOICES)
    specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    residence = models.CharField(max_length=50, choices=RESIDENCE_CHOICES)

    def __str__(self):
        return self.name
    
    
class StudentGroup(models.Model):
    name = models.CharField(max_length=100, unique=True)
    students = models.ManyToManyField(Student)  # Link students to groups

    def __str__(self):
        return self.name
    