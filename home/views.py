from django.shortcuts import render,redirect
from home.models import Student #Calling the function


# Create your views here.
def homepage(request):
    all_students = Student.objects.all() # We are accessing all students via students class
    total_students = len(all_students)

    total = 0
    for each in all_students:
        total = total + int(each.result)
    average = total / total_students    

    context = {
        'all_students': all_students,
        'total': total_students,
        'average': average
    }
    return render(request,'index.html',context)


def addpage(request):
    if request.method == 'POST':
        my_data = request.POST

        name = my_data['names']
        course = my_data['course']
        email = my_data['email']
        address = my_data['address']
        phone = my_data['phone']
        result = my_data['result']
        gender = my_data['gender']
        student_id = my_data['student_id']

        #The one on the left is the name in the class Student we created under models 
        # and the one on the right is the variable we have created above.

        new_student = Student()
        new_student.names = name
        new_student.course = course
        new_student.email = email
        new_student.address = address
        new_student.phone = phone
        new_student.result = result
        new_student.gender = gender
        new_student.student_id = student_id
        new_student.save()
        return redirect('/')
    
    return render(request,'add.html')

def viewpage(request, id):
    selected_student = Student.objects.get(id=id)
    
    return render(request, 'view.html')