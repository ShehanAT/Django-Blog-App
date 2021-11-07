import pytest 
import factory
from pytest_factoryboy import register
from rest_framework.test import APIClient, APIRequestFactory 
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django import VERSION as DJANGO_VERSION
from django.test import TestCase 
from django.urls import reverse 


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