import factory
from django.urls import reverse
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class InlineFeedbackFactory(factory.django.DjangoModelFactory):
    was_this_page_helpful = True
    location = "london"
    inline_feedback_choices = ""
    more_detail = ""

    class Meta:
        model = "inline_feedback.UserInlineFeedbackSurvey"


class InlineFeedbackAPI(TestCase):

    def test_unauthenticated_inline_feedback_should_redirect_to_auth(self):
        client = APIClient()
        response = client.post(reverse("inline_feedback:create"))
        assert response.status_code == status.HTTP_302_FOUND
        assert response.url == "/auth/login/?next=%2Fapi%2Fv1%2Finline_feedback"

    def test_creating_inline_feedback(self):
        User = get_user_model()
        user = User.objects.create_user(password="secret", username="ian")
        client = APIClient()
        client.force_login(user=user)
        response = client.post(
            reverse("inline_feedback:create"),
            {"location": "some location", "was_this_page_helpful": "true"},
        )
        assert len(response.json()) == 5
        assert response.json()["location"] == "some location"
        assert response.json()["was_this_page_helpful"] is True
        assert response.json()["inline_feedback_choices"] == ""
        assert response.json()["more_detail"] == ""
        assert response.status_code == status.HTTP_201_CREATED

    def test_updating_inline_feedback(self):

        User = get_user_model()
        user = User.objects.create_user(password="secret", username="ian")
        client = APIClient()
        client.force_login(user=user)
        feedback = InlineFeedbackFactory.create()
        response = client.patch(
            reverse("inline_feedback:update", args=f"{feedback.id}"),
            data={"inline_feedback_choices": "yes", "more_detail": "some details"},
        )
        assert response.json() == {
            "id": feedback.id,
            "location": feedback.location,
            "was_this_page_helpful": True,
            "inline_feedback_choices": "yes",
            "more_detail": "some details",
        }
        assert response.status_code == status.HTTP_200_OK
