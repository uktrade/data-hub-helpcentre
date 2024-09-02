from django.shortcuts import reverse
from django.test import TestCase


class PingdomTest(TestCase):
    def test_ping_response(self):
        url = reverse("pingdom")
        response = self.client.get(url)
        status_code = response.status_code
        content_type = response.headers["Content-Type"]

        self.assertTrue(status_code == 200 or status_code == 302)
        assert "<status>FALSE</status>" not in str(response.content)
        assert "text/xml" in content_type or "text/html" in content_type
