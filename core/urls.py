from django.urls import path

from .views import *

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

app_name = "core"

urlpatterns = [
                  path('', TemplateView.as_view(template_name='home.html'), name='home'),
                  path('invite/', InvitationView.as_view(), name = 'invite'),
                  path('course/', CourseView.as_view(), name='course'),
                  path('course-create/', CourseCreateView.as_view(), name='course-create'),                  
                  path('assignment-create/', AssignmentCreateView.as_view(), name='assignment-create'),
                  path('assignment/', AssignmentView.as_view(), name='assignment-list'),
                  path('<pk>/delete/', AssignmentDeleteView.as_view(), name='delete-assignment'),
                  path('assignment-submission/', AssignmentSubmissionView.as_view(), name='assignment-submission'),
                  path('assignment-submission-list/', AssignmentSubmissionListView, name='assignment-submission-list'),
                  path('<pk>/delete/', AssignmentSubmissionDelete.as_view(), name='assignment-submission-delete'),
                  path('assignment/feedback/',FeedbackSubmission,name='assignment-feedback'),
                  path('addInForum/',addInForum,name='addInForum'),
                  path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
                  path('ViewForum/',ViewForum,name='ViewForum'),
                 # path('ViewStats/',CourseStats,name='ViewStats'),
                  
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)