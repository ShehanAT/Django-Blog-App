import pytest 
from django.contrib.auth.models import User 
from django.test import TestCase 
from blogapp.models import Category, Post 
from django.urls import reverse 

class RouteTest(TestCase):

    @pytest.mark.django_db
    def test_homepage(self):
        homepage_url = reverse("blog:MainView")

        response = self.client.get(homepage_url)

        assert response.status_code == 200
        assert response.context["request"].path == "/"

    @pytest.mark.django_db 
    def test_no_access_page(self):
        no_access_url = reverse("blog:NoAccess")
        
        response = self.client.get(no_access_url)

        assert response.status_code == 200 
        assert response.context["request"].path == "/noaccess/"



