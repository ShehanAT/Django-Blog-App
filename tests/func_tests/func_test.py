from django.test import TestCase 
from selenium import webdriver 
import pytest 


class FunctionalTestCase(TestCase):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.browser = webdriver.Firefox()
        yield
        self.tearDown()

    @pytest.mark.django_db 
    def test_there_is_homepage(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Blog', self.browser.page_source)
        # assert True == True 

    
    def tearDown(self):
        self.browser.quit()