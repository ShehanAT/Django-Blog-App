from selenium import webdriver 

browser = webdriver.Firefox()
browser.get('http://localhost:8080')

assert browser.page_source.find("install")