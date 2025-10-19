from selenium.webdriver.common.by import By


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
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.set_enter()



    # Para assert
    def get_email_field(self):
        #return self._wait_for(self.email_field).get_property('value')
        return self.driver.find_element(*self.email_field).text


    def get_password_field(self):
        return self.driver.find_element(*self.password_field).text





