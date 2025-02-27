from django.urls import path
from .views import student_registration, group_students

urlpatterns = [
    path('register/', student_registration, name='register_student'),
    path('groups/', group_students, name='group_students'),
]
