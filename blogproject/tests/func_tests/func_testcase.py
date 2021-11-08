from django.test import TestCase 
from selenium import webdriver 


class FunctionalTestCase(TestCase):

    def setup(self):
        self.browser = webdriver.Firefox()

    def test_there_is_homepage(self):
        self.browser.get('http://localhost:7000')
        self.assertIn('install', self.browser.page_source)
        self.tearDown()

    def test_actions_dropdown_button(self):
        self.browser.get("http://localhost:7000")
        self.browser.find_element_by_class_name("dropdown-toggle").click()
        self.assertIn("", self.browser.page_source)
        print(self.browser.page_source)
        assert self.browser.page_source 

    def tearDown(self):
        self.browser.quit()
