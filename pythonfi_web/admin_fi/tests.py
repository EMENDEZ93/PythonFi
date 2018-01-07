from django.core.urlresolvers import reverse
from django.test import TestCase
from django.urls import resolve
from .login.views import signup

class SignupTest(TestCase):
    def test_signup_status_code(self):
        url = reverse('signup')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)


    def test_signup_url_resolver_signup_view(self):
        view = resolve('/signup/')
        self.assertEquals(view.func, signup)