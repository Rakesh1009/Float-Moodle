from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, CreateView, ListView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.http import Http404
from authentication.decorators import user_is_instructor, user_is_student
from core.forms import FeedbackForm
from core.models import AssignmentSubmission

from .forms import *
from .models import *

from .decorators import user_is_student, user_is_instructor
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from django.core.mail import EmailMessage, send_mail



class InvitationView(CreateView):
    template_name = 'core/instructor/invite.html'
    form_class = InvitationForm
    extra_context = {
        'title': 'New Course'
    }
    success_url = reverse_lazy('core:home')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'instructor':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(InvitationView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            x = form.save(commit=False)

            email_subject = "Invitation to join Float Moodle"
            email_body = f"Hi {x.sname}, You are invited to join float moodle by your professor. Follow this link to register as a student: https://floatmoodle-team-rocket.herokuapp.com/student/register"
            email = EmailMessage(
                email_subject,
                email_body,
                'noreply@moodle.com',
                [x.email]
            )
            email.send(fail_silently=False)
    
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




# COURSE CREATE VIEW
class CourseCreateView(CreateView):
    template_name = 'core/instructor/course_create.html'
    form_class = CourseCreateForm
    extra_context = {
        'title': 'New Course'
    }
    success_url = reverse_lazy('core:course')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'instructor':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CourseCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

class CourseView(ListView):
    model = Course
    template_name = 'core/instructor/courses.html'
    context_object_name = 'course'

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    # @method_decorator(user_is_instructor, user_is_student)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')  # filter(user_id=self.request.user.id).order_by('-id')


# ASSIGNMENT CREATE VIEW
class AssignmentCreateView(CreateView):
    template_name = 'core/instructor/assignment_create.html'
    form_class = AssignmentCreateForm
    extra_context = {
        'title': 'New Course'
    }
    success_url = reverse_lazy('core:assignment-list')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'instructor':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssignmentCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# VIEW FOR ASSIGNMENT LIST
class AssignmentView(ListView):
    model = Assignment
    template_name = 'core/instructor/assignments.html'
    context_object_name = 'assignment'

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    # @method_decorator(user_is_student, user_is_instructor)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.all()  # filter(user_id=self.request.user.id).order_by('-id')


# DELETE ASSIGNMENT VIEW
class AssignmentDeleteView(DeleteView):
    model = Assignment
    success_url = reverse_lazy('core:assignment-list')


# ASSIGNMENT SUBMISSION VIEW
class AssignmentSubmissionView(CreateView):
    template_name = 'core/instructor/assignment_submission.html'
    form_class = AssignmentSubmissionForm
    extra_context = {
        'title': 'New Exam'
    }
    success_url = reverse_lazy('core:home')

    @method_decorator(login_required(login_url=reverse_lazy('authentication:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('authentication:login')
        if self.request.user.is_authenticated and self.request.user.role != 'student':
            return reverse_lazy('authentication:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AssignmentSubmissionView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)




def AssignmentSubmissionListView(request):
    assignment_submission=AssignmentSubmission.objects.all()
    #count=foru.count()
    feedbacks=[]
    for i in assignment_submission:
        feedbacks.append(i.feedback_set.all())
 
    context={'assignment_submission':assignment_submission,'feedbacks':feedbacks}
    return render(request,'core/instructor/assignment_submission_list.html',context)


# EXAM DELETE VIEW
class AssignmentSubmissionDelete(DeleteView):
    model = AssignmentSubmission
    success_url = reverse_lazy('core:assignment-submission-list')






def FeedbackSubmission(request):
    form = FeedbackForm(request.POST)
    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            #return reverse_lazy('core/addInDiscussion.html')
            return redirect('core:assignment-submission-list')
    #success_url = reverse_lazy('core:ViewForum')   
    context ={'form':form}
    return render(request,'core/instructor/assignment_feedback.html',context)

def ViewForum(request):
    forums=forum.objects.all()
    count=forums.count()
    discussions=[]
    for i in forums:
        discussions.append(i.discussion_set.all())
 
    context={'forums':forums,
              'count':count,
              'discussions':discussions}
    return render(request,'core/ViewForum.html',context)
 
def addInForum(request):
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('core:ViewForum')
    #success_url = reverse_lazy('core:ViewForum')
    context ={'form':form}
    return render(request,'core/addInForum.html',context)
 
def addInDiscussion(request):
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            #return reverse_lazy('core/addInDiscussion.html')
            return redirect('core:ViewForum')
    #success_url = reverse_lazy('core:ViewForum')   
    context ={'form':form}
    return render(request,'core/addInDiscussion.html',context)

# def CourseStats(request):
#     grades = Feedback.objects.all()#filter(AssignmentSubmission.user=request.user)
    
#     courses = Course.objects.all()

#     mar_obtained = {}
#     total = {}

#     for c in courses:

#         mar_obtained[c.course_name] = 0
#         total[c.course_name] = 0
    


#     for foo in grades:

#         mar_obtained[foo.AssignmentSubmission.Assigment.Course.course_name] += foo.AssignmentSubmission.Assignment.weight*foo.marks
#         total[foo.AssignmentSubmission.Assigment.Course.course_name] += foo.AssignmentSubmission.Assignment.weight*foo.AssignmentSubmission.Assignment.marks


#     context = {
#         'mar_obtained' : mar_obtained,
#         'total' : total
#     }

#     return render(request, 'core/student/viewstats.html' ,context)