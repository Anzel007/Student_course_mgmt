from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from course.models import Course, StudentProfile
# def HomeView(request):
#     total_courses=Course.objects.count()
#     total_students=StudentProfile.objects.count()

#     output=f'''
#     Total students={total_students}
#     Total courses=={total_courses}
#     '''
    
#     return HttpResponse(output)
def HomeView(request):
    total_courses=Course.objects.count()
    total_students=StudentProfile.objects.count()

    output={
    'total_students':total_students,
    'total_courses':total_courses
    }
    
    return render(request,"index.html",output)

def StudentView(request):
    # i=0
    # student_data= StudentProfile.objects.get(id=i)
    student_data= StudentProfile.objects.all()
    # length=student_data.count()
    # output={
    #         # 'student_id':student_data.id,        
    #         'student_name':student_data.student_name,
    #         'grade':student_data.grade,
    #         'address':student_data.address,
    #         'blood_group':student_data.blood_group
    #         # 'length':length
    #     }
    
    # for data in Student.objects.all():
    #     student_dict.append(data)
        # output={
        # ''
        # }
    return render(request,"student.html",{'student_data':student_data})
def StudentAddView(request):
    return()

def CourseView(request):
    course_data=Course.objects.all()
    return render(request,"course.html",{'course_data':course_data})