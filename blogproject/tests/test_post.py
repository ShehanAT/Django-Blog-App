import pytest 
from django.contrib.auth.models import User
from django.test import TestCase 
from blogapp.models import Category, Post 
from django.db.utils import IntegrityError
from conftest import ConfTest

class PostTest(TestCase):

    @pytest.mark.django_db 
    def test_post_saves_when_author_present(self):
        new_post = Post()
        new_post.author = ConfTest.create_test_user(self)
        new_post.save()
        Post.objects.count() > 0

    @pytest.mark.django_db 
    def test_post_not_save_when_author_empty(self):
        new_post = Post() 
        with self.assertRaises(IntegrityError):
            new_post.save()  


    @pytest.mark.django_db 
    def test_new_post_has_zero_likes_after_saved(self):
        new_post = Post()
        new_post.author = ConfTest.create_test_user(self)
        new_post.save()
        assert new_post.likes == 0

          
