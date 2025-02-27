 
from django.shortcuts import render, redirect
from .models import Student , StudentGroup
from .forms import StudentForm
from collections import defaultdict
import random


def student_registration(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('group_students')
    else:
        form = StudentForm()
    return render(request, 'students/register.html', {'form': form})


def group_students(request):
    # Fetch all students and organize them by interest
    students_by_interest = defaultdict(list)
    all_students = Student.objects.all()

    for student in all_students:
        students_by_interest[student.interest].append(student)

    # Get the unique interests available
    unique_interests = list(students_by_interest.keys())

    # Prepare final groups
    final_groups = []
    group_count = 1
    StudentGroup.objects.all().delete()  # Clear old groups

    while all_students.exists():  # Keep forming groups until all students are placed
        group = []
        used_interests = set()

        for interest in unique_interests:
            if students_by_interest[interest]:  # If students of this interest are still available
                student = students_by_interest[interest].pop(0)  # Take one student
                group.append(student)
                used_interests.add(student.interest)

            if len(group) == 4:  # Stop when group reaches 4 students
                break

        if group:
            group_name = f"Group {group_count}"
            group_obj = StudentGroup.objects.create(name=group_name)
            group_obj.students.set(group)  # Assign students to the group
            final_groups.append((group_obj, group))
            group_count += 1

        # Update available students
        all_students = Student.objects.filter(id__in=[s.id for s_list in students_by_interest.values() for s in s_list])

    return render(request, 'students/groups.html', {'groups': final_groups})


