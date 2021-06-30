from django.db import models

# Create your models here.
class Student(models.Model):
    RollNo = models.CharField( max_length=11, primary_key = True)
    Password = models.CharField(max_length = 30)
    FName = models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    Email = models.EmailField()
    DOB = models.DateField()
    ContactNo = models.CharField(max_length=13)
    Placed = models.BooleanField(default=False)
    def __str__(self):
        return self.RollNo

class Course(models.Model):
    RollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    COrg = models.CharField(max_length = 200)
    CName = models.CharField(max_length = 200)
    CID = models.CharField(max_length = 200)
    CLink = models.URLField(max_length = 300)
    def __str__(self):
        return self.RollNo

class Skill(models.Model):
    RollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    SName = models.CharField(max_length = 200)
    def __str__(self):
        return self.RollNo

class Project(models.Model):
    RollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    PName = models.CharField(max_length=200)
    PLink = models.URLField(max_length = 300)
    def __str__(self):
        return self.RollNo

class Mark(models.Model):
    RollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    sem1 = models.IntegerField()
    sem2 = models.IntegerField()
    sem3 = models.IntegerField()
    sem4 = models.IntegerField()
    sem5 = models.IntegerField()
    sem6 = models.IntegerField()
    sem7 = models.IntegerField()
    sem8 = models.IntegerField()
    def __str__(self):
        return self.RollNo

class Admin(models.Model):
    Id = models.CharField(max_length=100, primary_key = True)
    Pass = models.CharField(max_length = 100)
    def __str__(self):
        return self.Id
class Profile(models.Model):
    RollNo = models.ForeignKey(Student, on_delete=models.CASCADE)
    username =models.CharField(max_length=100)
    PURL = models.URLField(max_length=300)
    Website = models.URLField(max_length=300)
    def __str__(self):
        return self.RollNo

class Records(models.Model):
    CName = models.CharField(max_length=100,primary_key=True)
    NoStudent = models.IntegerField()
    AvgPack = models.IntegerField()
    def __str__(self):
        return self.CName
    
class UCompany(models.Model):
    CName = models.CharField(max_length = 200)
    JTitle = models.CharField(max_length = 200)
    Avg = models.IntegerField()
    Date = models.DateField()
    def __str__(self):
        return self.CName
    
    

    


