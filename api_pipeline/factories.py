import string
import factory
from datetime import datetime
from factory.fuzzy import FuzzyText


class UserInlineFeedbackSurveyFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = "inline_feedback.UserInlineFeedbackSurvey"

    created_date = datetime.now()
    modified_date = datetime.now()
    location = FuzzyText(length=4, chars=string.digits, suffix="%")
    was_this_page_helpful = True
    inline_feedback_choices = FuzzyText(length=6, chars=string.digits, suffix="%")
    more_detail = FuzzyText(length=2, chars=string.digits, suffix="%")
