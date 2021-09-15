import datetime

from django.test import (
    TestCase,
    override_settings,
)

from freezegun import freeze_time

import mohawk

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from wagtail.tests.utils import WagtailPageTests
from .models import (
    ArticlePage,
    ArticleIndexPage,
)

from home.models import HomePage


# noinspection PyMethodMayBeStatic
class ArticleIndexPageTests(WagtailPageTests):
    def test_cannot_create_article_page_under_homepage(self):
        self.assertCanNotCreateAt(HomePage, ArticlePage)

    def test_can_create_article_page_index_index_page(self):
        self.assertCanCreateAt(ArticleIndexPage, ArticlePage)

test_url = "http://testserver" + reverse("child_article_feed", kwargs={"path": "data-hub/updates/"})


def hawk_auth_sender(
    key_id="access_key",
    secret_key="secret_key",
    url=test_url,
    method="GET",
    content_type="application/json",
):
    return mohawk.Sender(
        {"id": key_id, "key": secret_key, "algorithm": "sha256",},
        url,
        method,
        content="",
        content_type=content_type,
    )


class HawkTests(TestCase):
    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="access_key", HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_empty_object_returned_with_authentication(self):
        """If the Authorization and X-Forwarded-For headers are correct, then
        the correct, and authentic, data is returned
        """
        sender = hawk_auth_sender()
        response = APIClient().get(
            test_url,
            content_type="application/json",
            HTTP_AUTHORIZATION=sender.request_header,
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )
        assert response.status_code == status.HTTP_404_NOT_FOUND

    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="wrong-id", HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_bad_credentials_mean_401_returned(self):
        """If the wrong credentials are used,
        then a 401 is returned
        """
        sender = hawk_auth_sender()
        response = APIClient().get(
            test_url,
            content_type="application/json",
            HTTP_AUTHORIZATION=sender.request_header,
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    @override_settings(
        HAWK_INCOMING_ACCESS_KEY="access_key", HAWK_INCOMING_SECRET_KEY="secret_key",
    )
    def test_if_61_seconds_in_past_401_returned(self):
        """If the Authorization header is generated 61 seconds in the past, then a
        401 is returned
        """
        past = datetime.datetime.now() - datetime.timedelta(seconds=61)
        with freeze_time(past):
            auth = hawk_auth_sender().request_header
        response = APIClient().get(
            test_url,
            content_type="",
            HTTP_AUTHORIZATION=auth,
            HTTP_X_FORWARDED_FOR="1.2.3.4, 123.123.123.123",
        )

        assert response.status_code == status.HTTP_401_UNAUTHORIZED
