from django.contrib import admin
from .models import Course, Student, Lesson, Order

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Lesson)
admin.site.register(Order)
