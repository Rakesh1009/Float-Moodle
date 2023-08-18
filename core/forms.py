from django import forms

from core.models import AssignmentSubmission, Feedback
from .models import *


class InvitationForm(forms.ModelForm):
    class Meta:
        model = Invitation
        fields = ['sname', 'email']

    def __init__(self, *args, **kwargs):
        super(InvitationForm, self).__init__(*args, **kwargs)
        self.fields['sname'].label = "Student Name"
        self.fields['email'].label = "Student Email"

        self.fields['sname'].widget.attrs.update(
            {
                'placeholder': 'Enter Student Name',
            }
        )

        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Student Email',
            }
        )

    def is_valid(self):
        valid = super(InvitationForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(InvitationForm, self).save(commit=False)
        if commit:
            course.save()
        return course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'course_description', 'end_date']

    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].label = "Course Name"
        self.fields['course_description'].label = "Description"
        self.fields['end_date'].label = "End Date"

        self.fields['course_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Course Name',
            }
        )

        self.fields['course_description'].widget.attrs.update(
            {
                'placeholder': 'Description',
            }
        )

    def is_valid(self):
        valid = super(CourseCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(CourseCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course

        
# ASSIGNMENT CREATE FORM
class AssignmentCreateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['Course','title', 'content', 'weight', 'duration','end_at']
        #fields = ['title', 'content', 'marks', 'duration']

    

    def is_valid(self):
        valid = super(AssignmentCreateForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentCreateForm, self).save(commit=False)
        if commit:
            course.save()
        return course

class AssignmentSubmissionForm(forms.ModelForm):
    class Meta:
        model= AssignmentSubmission
        fields = ['Assignment','content','file']

    def is_valid(self):
        valid = super(AssignmentSubmissionForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(AssignmentSubmissionForm, self).save(commit=False)
        if commit:
            course.save()
        return course




class FeedbackForm(forms.ModelForm):
    class Meta:
        model= Feedback
        fields = "__all__"

    def is_valid(self):
        valid = super(FeedbackForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(FeedbackForm, self).save(commit=False)
        if commit:
            course.save()
        return course



class CreateInForum(forms.ModelForm):
    class Meta:
        model= forum
        fields = ['topic']
    
    def is_valid(self):
        valid = super(CreateInForum, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(CreateInForum, self).save(commit=False)
        if commit:
            course.save()
        return course

 
class CreateInDiscussion(forms.ModelForm):
    class Meta:
        model= Discussion
        fields = ['forum','discuss']

    def is_valid(self):
        valid = super(CreateInDiscussion, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    def save(self, commit=True):
        course = super(CreateInDiscussion, self).save(commit=False)
        if commit:
            course.save()
        return course
