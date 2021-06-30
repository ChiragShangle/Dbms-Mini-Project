from django.db.models.fields import EmailField
from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
from django.core import serializers
from json import dumps
import json
from rest_framework.renderers import JSONRenderer


# Create your views here.
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('student')
    return render(request,'home.html')
def project(request):
    username=request.user.username
    if request.method=='POST':
        PName = request.POST.get('PName')
        PLink = request.POST.get('PLink')
        obj = Student.objects.get(RollNo=username)
        obj2 = Project(RollNo=obj,PName=PName,PLink=PLink)
        obj2.save()
        return redirect('student')

def profile(request):
    uname = request.user.username
    if request.method=='POST':
        username = request.POST.get('username')
        PURL = request.POST.get('PURL')
        Website = request.POST.get('Website')
        obj = Student.objects.get(RollNo=uname)
        obj2 = Profile(RollNo=obj,username=username,PURL=PURL,Website=Website)
        obj2.save()
        return redirect('student')
def record(request):
    if request.method=='POST':
        CName = request.POST.get('CName')
        NoStudent = request.POST.get('NoStudent')
        AvgPack = request.POST.get('AvgPack')
        obj = Records(CName=CName, NoStudent=NoStudent, AvgPack=AvgPack)
        obj.save()
        return redirect('admin')
def upcom(request):
    if request.method == 'POST':
        CName =request.POST.get('CName')
        JTitle = request.POST.get('JTitle')
        Avg = request.POST.get('Avg')
        Date = request.POST.get('Date')
        obj = UCompany(CName=CName,JTitle=JTitle,Avg=Avg,Date=Date)
        obj.save()
        return redirect('admin')

def academics(request):
    if request.method=='POST':
        RollNo=request.POST.get('RollNo')
        semester = request.POST.get('semester')
        marks = request.POST.get('marks')

        obj = Student.objects.get(RollNo=RollNo)
        if semester == "sem1":
            obj2 = Mark(RollNo=obj,sem1=marks,sem2=0,sem3=0,sem4=0,sem5=0,sem6=0,sem7=0,sem8=0)
        elif semester == "sem2":
            obj2 =  Mark(RollNo=obj,sem1=0,sem2=marks,sem3=0,sem4=0,sem5=0,sem6=0,sem7=0,sem8=0)
        elif semester == "sem3":
            obj2 = Mark(RollNo=obj,sem1=0,sem2=0,sem3=marks,sem4=0,sem5=0,sem6=0,sem7=0,sem8=0)
        elif semester == "sem4":
            obj2 =  Mark(RollNo=obj,sem1=0,sem2=0,sem3=0,sem4=marks,sem5=0,sem6=0,sem7=0,sem8=0)
        elif semester == "sem5":
            obj2 =  Mark(RollNo=obj,sem1=0,sem2=0,sem3=0,sem4=0,sem5=marks,sem6=0,sem7=0,sem8=0)
        elif semester == "sem6":
            obj2 =  Mark(RollNo=obj,sem1=0,sem2=0,sem3=0,sem4=0,sem5=0,sem6=marks,sem7=0,sem8=0)
        elif semester == "sem7":
            obj2 =  Mark(RollNo=obj,sem1=0,sem2=0,sem3=0,sem4=0,sem5=0,sem6=0,sem7=marks,sem8=0)
        else:
            obj2 =  Mark(RollNo=obj,sem1=0,sem2=0,sem3=0,sem4=0,sem5=0,sem6=0,sem7=0,sem8=marks)
        obj2.save()
        return redirect('admin')



def course(request):
    return render(request,'courses.html')

def edit(request):
    username = request.user.username
    
    if request.method=='POST':
       
        fname = request.POST.get('ufName')
        lname = request.POST.get('ulName')
        email = request.POST.get('uEmail')
        password = request.POST.get('uPass')
        cpassword = request.POST.get('ucPass')
        dob = request.POST.get('dob')
        phone = request.POST.get('upNum')
        skills = request.POST.get('skills')
        if password != cpassword:
            mess = {'abcd': 'BOTH PASSWORDS MUST BE SAME!'}
            return render(request, 'edit.html',mess)
        obj = Student(RollNo=username, Password=password, FName=fname, LName=lname, Email=email, DOB=dob, ContactNo=phone)
        obj.save()
        i=0
        j=0
        for s in skills:
            
            if s==',':
                x=skills[j:i]
                obj1=Skill(RollNo=obj,SName=x)
                obj1.save()
                j=i+1
            i=i+1
        x=skills[j:i]
        obj1=Skill(RollNo=obj,SName=x)
        obj1.save()
        redirect('student')

        
    return render(request,'edit.html')

def logout_user(request):
    if request.method=='GET':
        logout(request)
        return redirect('home')
def loginuser(request):
    if request.user.is_authenticated:
        return redirect('student')
    else:
        if request.method=='POST':
            username= request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('student')
            else:
                messages.error(request,'Roll No. or Password is Incorrect')
                return redirect('login')
        return render(request,'login.html')
def mailuser(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        message = request.POST.get('message')
        email_from = settings.EMAIL_HOST_USER
        send_mail( name,message, email_from, [email])
        return redirect('home')
    return render(request,'home.html')
def student(request):
    username = request.user.username
    student = Student.objects.filter(RollNo=username)
    skill = Skill.objects.filter(RollNo=username)
    project = Project.objects.filter(RollNo=username)
    profile = Profile.objects.filter(RollNo=username)
    course = Course.objects.filter(RollNo=username)
    record = Records.objects.all()
    upcoming = UCompany.objects.all()
    marks = Mark.objects.filter(RollNo=username)
    # marks = dumps(marks)
    
    context  = {'student':student,'skill':skill,'project':project,'profile':profile,'course':course,'record':record,'upcoming':upcoming,'marks':marks}
    
    
    return render(request, 'student_dashboard.html',{"context":context})


def register(request):
    if request.method == 'POST':
        fname = request.POST.get('ufName')
        lname = request.POST.get('ulName')
        email = request.POST.get('uEmail')
        password = request.POST.get('uPass')
        cpassword = request.POST.get('ucPass')
        dob = request.POST.get('dob')
        phone = request.POST.get('upNum')
        rollno = request.POST.get('rollno')
        
        if password != cpassword:
            mess = {'abcd': 'BOTH PASSWORDS MUST BE SAME!'}
            return render(request, 'register.html',mess)

        if User.objects.filter(username=rollno).exists():
            mess = {'abcd':'USER ALREADY EXIST!'}
            return render(request,'login.html',mess)
        else:
            obj = Student(RollNo=rollno, Password=password, FName=fname, LName=lname, Email=email, DOB=dob, ContactNo=phone)
            obj.save()
            user=User.objects.create_user(username=rollno,password=password)
            user.save()
            user=authenticate(username=rollno,password=password)
            if user is not None:
                login(request,user)
                return redirect('student')
            else:
                messsages.error(request,'username or password not correct')
                return redirect('login')
    return render(request,'register.html')
def adminn(request):
    student = Student.objects.all()
    mark = Mark.objects.all()
    marks ={}
    for j in student:
        for x in mark:
            count =0
            sum=0
            if x.sem1!=0:
                count =count+1
                sum=sum+x.sem1/1300
            if x.sem2!=0:
                count =count+1
                sum=sum+x.sem2/1200
            if x.sem3!=0:
                count =count+1
                sum=sum+x.sem3/1000
            if x.sem4!=0:
                count =count+1
                sum=sum+x.sem4/1200
            if x.sem5!=0:
                count =count+1
                sum=sum+x.sem5/1200
            if x.sem6!=0:
                count =count+1
                sum=sum+x.sem6/1000
            if x.sem7!=0:
                count =count+1
                sum=sum+x.sem7/1100
            if x.sem8!=0:
                count =count+1
                sum=sum+x.sem8/1000
            
            temp=round((sum/count)*100) 
            marks.setdefault(j.RollNo, []).append(temp)
            marks.setdefault(j.RollNo, []).append(j.FName)
            marks.setdefault(j.RollNo, []).append(j.LName)
            marks.setdefault(j.RollNo, []).append(j.Placed)


    context={'marks':marks}
    
    return render(request,'admin.html',{'context':context})
def organization(request):
    username = request.user.username
    if request.method=='POST':
        COrg = request.POST.get('COrg')
        CName = request.POST.get('CName')
        CID = request.POST.get('CID')
        CLink = request.POST.get('CLink')
        obj2 = Student.objects.get(RollNo=username)
        obj = Course(RollNo=obj2,COrg=COrg, CName=CName, CID=CID, CLink=CLink)
        obj.save()
        return redirect('organization')
    return redirect('student')

def adminlogin(request):
    return render(request,'adminlogin.html')
def adminauth(request):
    if request.method =='POST':
        Id = request.POST.get('Id')
        Pass = request.POST.get('Pass')
        if Admin.objects.filter(Id=Id,Pass=Pass).exists():
            return redirect('admin')
        else:
            messages.error(request,'ID or Password is Incorrect')
            return redirect('adminlogin')


