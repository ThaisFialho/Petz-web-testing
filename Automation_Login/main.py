from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
import data
from page import PetzPage

class TestPetz:

    def test_set_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(data.PETZ_URL)
        self.petz = PetzPage(self.driver)
        email = data.EMAIL
        password = data.PASSWORD
        self.petz.set_login(email,password)
        assert self.petz.get_email_field() == email
        assert self.petz.get_password_field() == password
        self.driver.quit()






