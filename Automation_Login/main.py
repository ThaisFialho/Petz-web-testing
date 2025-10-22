from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import data
from page import PetzPage

class TestPetz:

    def test_set_login(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(data.PETZ_URL)
        self.petz = PetzPage(self.driver)
        email = data.EMAIL
        password = data.PASSWORD
        self.petz.set_login(email, password)
        self.petz.set_enter()
        assert self.petz.get_email_field() == email
        assert self.petz.get_password_field() == password
        self.driver.quit()