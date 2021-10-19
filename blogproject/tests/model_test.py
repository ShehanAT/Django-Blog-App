import pytest 
from django.contrib.auth.models import User
from django.test import TestCase 
from blogapp.models import Category, Post 

class ModelTest(TestCase):

    @pytest.mark.django_db 
    def test_category_model_persists(self):
        new_category = Category()

        new_category.name = "new_category"
        new_category.save()

        assert new_category.name == "new_category"
        assert Category.objects.count() > 0

    
    @pytest.mark.django_db 
    def test_post_model_persists(self):
        new_post = Post()
        new_post.title = "new_post"

        posted_user = User(
            username="test_user",
            email="test_user@test_user.com",
            password="test_user"
        )
        
        posted_user.save()

        new_post.author = posted_user

        old_post_obj_count = Post.objects.filter().count() 
        new_post.save()
        new_post_obj_count = Post.objects.filter().count() 

        assert new_post.title == "new_post"
        assert old_post_obj_count < new_post_obj_count



