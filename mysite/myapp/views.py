from django.shortcuts import render
from django.http import HttpResponse
from .models import Form_1
# Create your views here.
def index(request):
  if request.method == "POST":
    form = Form_1()
    name = request.POST.get('name')
    email = request.POST.get('email')
    age = request.POST.get('age')
    college = request.POST.get('college')
    rollno = request.POST.get('rollno')
    year = request.POST.get('year')
    branch = request.POST.get('branch')
    interests = request.POST.get('interests')
    form.name = name
    form.email = email
    form.age = age
    form.college = college
    form.rollno = rollno
    form.year =year
    form.branch = branch
    form.interests =interests
    form.save()
    return HttpResponse("<h1>Thanks for Submitting Form </</h1>")
  return render(request,'index.html')
