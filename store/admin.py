from django.contrib import admin

# Register your models here.

from .models import Department, Course, Purpose, Student, Material

admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Purpose)
admin.site.register(Student)
admin.site.register(Material)
