from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setup(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            'zzc@gmail.com',
            'admin123'
        )
        self.client.force_login(self.admin_user)

        self.user = get_user_model().objects.create_user(
            'jessie@gmail.com',
            'test123',
            name='jessica'
        )

    def test_user_listed(self):
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
