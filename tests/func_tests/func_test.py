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

    @pytest.mark.django_db 
    def test_actions_dropdown_button_works(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_class_name("dropdown-toggle").click()
        # FIND WAY TO CHECK IF 'All Articles' <a/> IS VISIBLE
        self.assertIn("All Articles", self.browser.page_source)
        self.browser.find_element_by_xpath("//a[contains(text(), 'All Articles')]")
    
    def tearDown(self):
        self.browser.quit()