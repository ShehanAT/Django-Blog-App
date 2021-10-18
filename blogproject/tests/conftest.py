import pytest
from django.contrib.auth.models import User
from django.test import TestCase 


class ConfTest(TestCase):

    @pytest.mark.django_db
    def test_register_success(self):
        superuser = User.objects.create_superuser(
            username="admin",
            email="admin@admin.com",
            password="admin"
        );

        superuser.save();
        assert User.objects.count() > 0
