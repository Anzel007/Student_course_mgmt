from django.db import models


# Create your models here.
class StudentProfile(models.Model):
    student_name = models.CharField(max_length=100, null=True, blank=True)
    grade = models.CharField(max_length=100, null=True, blank=True)
    address = models.TextField(max_length=100, null=True, blank=True)
    blood_group = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.student_name


class Course(models.Model):
    coursename = models.CharField(max_length=100)
    coursedetails = models.TextField(max_length=200)
    instructor = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.DateField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.coursename
        # return(f{})

    # student=models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    student = models.ForeignKey(
        StudentProfile, on_delete=models.CASCADE, null=True, blank=True
    )


# class Datab(models.Model):
