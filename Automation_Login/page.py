from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PetzPage:

    #Localizadores
    email_field = (By.ID, 'loginEmail')
    password_field = (By.ID, 'loginPassword')
    enter_button = (By.XPATH, '//strong[contains(text(), "ENTRAR")]')

    def __init__(self, driver):
        self.driver = driver

     # Metodo para a função teste_set_login
    def set_enter(self):
        self.driver.find_element(*self.enter_button).click()

    def set_login(self,email,password):
        wait = WebDriverWait(self.driver, 20)

        # Fecha o banner de cookies, se aparecer
        try:
            cookies_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookies_btn.click()
        except:
            pass

        # Espera o campo de e-mail ficar visível e interagível
        email_input = wait.until(EC.visibility_of_element_located(self.email_field))
        # Garante que nenhum overlay esteja bloqueando
        self.driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
        self.driver.execute_script("arguments[0].focus();", email_input)
        email_input.clear()
        email_input.send_keys(email)
        password_input = wait.until(EC.visibility_of_element_located(self.password_field))
        password_input.clear()
        password_input.send_keys(password)


        #self.driver.find_element(*self.email_field).send_keys(email)
        #self.driver.find_element(*self.password_field).send_keys(password)
        #self.set_enter()


    # Para assert
    def get_email_field(self):
        return self.driver.find_element(*self.email_field).get_attribute('value')


    def get_password_field(self):
        return self.driver.find_element(*self.password_field).get_attribute('value')





