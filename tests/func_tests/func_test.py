from django.test import TestCase 
from selenium import webdriver 
import pytest 


class FunctionalTestCase(TestCase):
    LOGIN_URL = 'http://localhost:8000/login/'    
    ADMIN_URL = 'http://localhost:8000/admin/login/?next=/admin/'
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
        all_articles_btn = self.browser.find_element_by_xpath("//a[contains(text(), 'All Articles')]")
        if all_articles_btn.is_displayed():
            assert True 
        else: 
            pytest.fail() 

    @pytest.mark.django_db 
    def test_post_link_works(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_class_name("dropdown-toggle").click()
   
        old_url = self.browser.current_url
        first_post_link = self.browser.find_element_by_xpath("//a[contains(@href, '/post/2')]").click()
        # all_articles_btn = self.browser.find_element_by_xpath("//a[contains(text(), 'All Articles')]")
        new_url = self.browser.current_url
        if old_url != new_url:
            assert True 
        else:
            pytest.fail()

    @pytest.mark.django_db
    def test_login_btn_works(self):
        self.browser.get("http://localhost:8000")
        self.browser.find_element_by_xpath("//a[contains(@href, '/login/')]").click()
        login_url = self.browser.current_url 
        if login_url == self.LOGIN_URL:
            assert True 
        else:
            pytest.fail()

    @pytest.mark.django_db
    def test_admin_link_works(self):
        self.browser.get("http://localhost:8000")
        self.browser.find_element_by_xpath("//a[contains(@href, '/admin/')]").click()
        admin_url = self.browser.current_url 
        if admin_url == self.ADMIN_URL:
            assert True 
        else:
            pytest.fail()

    def tearDown(self):
        self.browser.quit()