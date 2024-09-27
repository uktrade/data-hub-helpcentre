from rest_framework import serializers

from inline_feedback.models import UserInlineFeedbackSurvey


class UserInlineFeedbackSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInlineFeedbackSurvey
        fields = "__all__"
