from django.contrib import admin
from .models import Student, StudentGroup

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'interest', 'specialization', 'residence')

class StudentGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('students',)  

admin.site.register(Student, StudentAdmin)
admin.site.register(StudentGroup, StudentGroupAdmin)
