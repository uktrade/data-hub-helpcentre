from django.db import models


class UserInlineFeedbackSurvey(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    location = models.CharField(max_length=256)
    was_this_page_helpful = models.BooleanField(null=False, blank=False)
    inline_feedback_choices = models.TextField(null=True, blank=True)
    more_detail = models.TextField(null=True, blank=True)
