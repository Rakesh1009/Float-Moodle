from django.contrib import admin

from core.models import Feedback
from .models import *

admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(AssignmentSubmission)
admin.site.register(Feedback)
admin.site.register(forum)
admin.site.register(Discussion)
admin.site.register(Invitation)
