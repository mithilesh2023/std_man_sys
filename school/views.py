from django.shortcuts import render,redirect
from .forms import StudentForm
from .models import Students
# Create your views here.
def homepage(req):
    form = StudentForm(req.POST or None)
    data = {
        "students" : Students.objects.all(),
        "form" : form
    }

    if req.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(homepage)
    
    return render(req,"index.html",data)


def deleteStudent(req, id):
    student = Students.objects.get(pk=id)
    student.delete()
    return redirect(homepage)

def editStudent(req,id):
        student=Students.objects.get(pk=id)
        form=StudentForm(req.POST or None,instance=student)

        if req.method =="POST":
            if form.is_valid():
                form.save()
                return redirect(homepage)
                
        return render(req,"edit.html",{"form":form})