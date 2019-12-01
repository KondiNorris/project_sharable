from django.shortcuts import render
from .models import User, Student, Teacher
from django.contrib.auth.decorators import login_required
from .forms import StudentCreationForm


""" def studentreg(request):
    if request.method == 'POST':
        form = StudentCreationForm()
    return render(request, 'users/studentreg.html', {form: 'form'}) """

# @login_required


def studentreg(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        mname = request.POST.get('middle_name')
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        # active = request.POST.get('active')
        admission_number = request.POST.get('admission_number')
        grade = request.POST.get('grade')
        student = Student.objects.create(admission_number=admission_number, grade=grade, active=active,
                                         first_name=first_name, last_name=lname, middle_name=mname, gender=gender)
        student.save()
        content = {fname: 'fname', mname: 'mname', lname: 'lname', gender: 'gender',
                   role: 'role', admission_number: 'admission_number', grade: 'grade'}
        return render(request, 'users/studentreg.html', {})


"""@login_required
def studentupdate(request):
    if request.method == 'POST':
        fname = request.POST.get('first_name')
        lname = request.POST.get('last_name')
        mname = request.POST.get('middle_name')
        gender = request.POST.get('gender')
        role = request.POST.get('role')
        active = request.POST.get('active')
           admission_number = request.POST.get('admission_number')
           grade = request.POST.get('grade')
           student = Student.objects.filter(admission_number=admission_number).update(admission_number=admission_number, grade=grade, active=active,
                                                                                      first_name=first_name, last_name=lname, middle_name=mname, gender=gender)
           student.save()
           return redirect('library-home')


   @login_required
   def teacherreg(request):
       if request.method == 'POST':
           fname = request.POST.get('first_name')
           lname = request.POST.get('last_name')
           mname = request.POST.get('middle_name')
           gender = request.POST.get('gender')
           role = request.POST.get('role')
           active = request.POST.get('active')
           teacher_email = request.POST.get('teacher_email')
           teacher = Teacher.objects.create(teacher_email=teacher_email).update(
               first_name=first_name, last_name=lname, middle_name=mname, gender=gender, role=role, active=active)
           teacher.save()
           return redirect('library-home')


   @login_required
   def teacherupdate(request):
       if request.method == 'POST':
           fname = request.POST.get('first_name')
           lname = request.POST.get('last_name')
           mname = request.POST.get('middle_name')
           gender = request.POST.get('gender')
           role = request.POST.get('role')
           active = request.POST.get('active')
           teacher_email = request.POST.get('teacher_email')
           teacher = Teacher.objects.update(teacher_email=teacher_email).update(
               first_name=first_name, last_name=lname, middle_name=mname, gender=gender, role=role, active=active)
           teacher.save()
           return redirect('library-home')


   @login_required
   def studentdelete(request):
       if request.method == 'POST':
           admission_number = request.POST.get('admission_number')
           student = Student.objects.filter(
               admission_number=admission_number).delete()
           stuudent.save()
           return redirect('library-home')


   @login_required
   def teacherdelete(request):
       if request.method == 'POST':
           teacher_email = request.POST.get('teacher_email')
           teacher = Teacher.objects.filter(teacher_email=teacher_email).delete()
           teacher.save()
           return redirect('library-home')"""
