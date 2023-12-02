from django.contrib import admin

# Register your models here.
from .models import Course, StudentProfile


class CourseAdmin(admin.ModelAdmin):
    list_display=["id","coursename","instructor","start_date","custom_field"]
    fields=["coursename","instructor"]
    def custom_field(self,obj):
        return f"Field:{obj.id}"
#to allow editing selective fields
admin.site.register(Course, CourseAdmin)


class StudentProfileAdmin(admin.ModelAdmin):
    list_display=["id","student_name","grade","address"]


admin.site.register(StudentProfile, StudentProfileAdmin)
# admin.site.register()

