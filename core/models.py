from django.db import models
from authentication.models import User
from django.utils import timezone

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_description = models.TextField()
    created_at = models.DateField(default=timezone.now)
    end_date = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name


# Create your models here.
class Assignment(models.Model):
    Course = models.ForeignKey(Course,blank=True,on_delete=models.CASCADE,null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    #marks = models.CharField(max_length=20)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=timezone.now())
    end_at = models.DateTimeField(null=True,blank=True)
    weight = models.IntegerField()


    def __str__(self):
        return '{}:{}'.format(str(self.Course),str(self.title))


class AssignmentSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Assignment = models.ForeignKey(Assignment,blank=True,on_delete=models.CASCADE,null=True)
    #assignment_name = models.CharField(max_length=500,default='uk')
    #name = models.CharField(max_length=100)
    #university_id = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    #feedback = models.CharField(max_length=200)
    file = models.FileField(upload_to='submissions/',null=True, blank=True)

    def __str__(self):
        return '{}:{}'.format(str(self.Assignment),str(self.user))

class Feedback(models.Model):
    AssignmentSubmission = models.ForeignKey(AssignmentSubmission,blank=True,on_delete=models.CASCADE)
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback = models.CharField(max_length=200)
    marks = models.IntegerField()

    def __str__(self):
        return str(self.AssignmentSubmission)

class forum(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #forum_id = models.AutoField
    #name=models.CharField(max_length=200,default="anonymous" )
    #name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    #email=models.CharField(max_length=200,null=True)
    topic= models.CharField(max_length=300)
    #description = models.CharField(max_length=1000,blank=True)
    #link = models.CharField(max_length=100 ,null =True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.topic)
 
#child model
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    #discussion_id = models.AutoField
    #name1=models.CharField(max_length=200,default="anonymous" )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discuss = models.CharField(max_length=1000)
 
    def __str__(self):
        return str(self.forum)

class Invitation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sname = models.CharField(max_length=100)
    email = models.EmailField()