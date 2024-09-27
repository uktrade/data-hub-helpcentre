import datetime
import mohawk
from django.test import override_settings
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from api_pipeline.factories import UserInlineFeedbackSurveyFactory


User = get_user_model()

test_url = "http://testserver" + reverse("user-inline-feedback-survey")


def hawk_auth_sender(
    key_id="access_key",
    secret_key="secret_key",
    url=test_url,
    method="GET",
    content_type="application/json",
    timestamp=None,
):
    if timestamp is None:
        timestamp = int(datetime.datetime.now().timestamp())

    sender = mohawk.Sender(
        {
            "id": key_id,
            "key": secret_key,
            "algorithm": "sha256",
        },
        url,
        method,
        content="",
        content_type=content_type,
    )

    sender.timestamp = timestamp
    request_header = sender.request_header

    return request_header


class TestHawkTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="access_key",
        HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_empty_object_returned_with_authentication(self):
        """If the Authorization and X-Forwarded-For headers are correct, then
        the correct, and authentic, data is returned
        """
        sender = hawk_auth_sender()
        response = self.client.get(
            test_url,
            content_type="application/json",
            HTTP_AUTHORIZATION=sender,
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )
        assert response.status_code == status.HTTP_200_OK
        assert response.data == []

    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="access_key",
        HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_object_returned_with_authentication(self):
        """If the Authorization and X-Forwarded-For headers are correct, then
        the correct, and authentic, data is returned
        """
        feedback1 = UserInlineFeedbackSurveyFactory()
        sender = hawk_auth_sender()
        response = self.client.get(
            test_url,
            content_type="application/json",
            HTTP_AUTHORIZATION=sender,
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )
        year = datetime.date.today().year
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()[0]) == 7
        assert response.json()[0]["id"] == feedback1.id
        assert str(year) in response.json()[0]["created_date"]
        assert str(year) in response.json()[0]["modified_date"]
        assert response.json()[0]["location"] == feedback1.location
        assert (
            response.json()[0]["was_this_page_helpful"]
            == feedback1.was_this_page_helpful
        )
        assert (
            response.json()[0]["inline_feedback_choices"]
            == feedback1.inline_feedback_choices
        )
        assert response.json()[0]["more_detail"] == feedback1.more_detail

    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="wrong-id",
        HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_bad_credentials_mean_401_returned(self):
        """If the wrong credentials are used, then a 401 is returned."""
        sender = hawk_auth_sender()
        response = self.client.get(
            test_url,
            content_type="application/json",
            HTTP_AUTHORIZATION=sender,
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="access_key",
        HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_missing_authorization_header(self):
        """If the Authorization header is missing, then a 401 is returned."""
        response = self.client.get(
            test_url,
            content_type="application/json",
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
