import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep



class MediaExRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.mediaexpert.pl/")

    def testWrongEmail(self):
        driver = self.driver
        action = webdriver.ActionChains(driver)
        twoje_konto = WebDriverWait(driver, 30).until(EC.element_to_be_clickable\
        ((By.XPATH, '//span[contains(text(), "Twoje konto")]')))
        action.move_to_element(twoje_konto)
        action.perform()
        zaloguj = WebDriverWait(driver, 30).until(EC.element_to_be_clickable\
        ((By.XPATH, '//a[@class="c-btn is-link is-small is-registerBtn"]')))
        zaloguj.click()
        name_field = driver.find_element_by_id('enp_customer_registration_form_type_address_firstName')
        name_field.send_keys("Sylwia")
        nazwisko_field = driver.find_element_by_id('enp_customer_registration_form_type_address_lastName')
        nazwisko_field.send_keys("Czerwiec")
        email = driver.find_element_by_id('enp_customer_registration_form_type_email')
        email.send_keys("<sylwiaczerwiec@wp.pl")
        password = driver.find_element_by_id('enp_customer_registration_form_type_plainPassword')
        password.send_keys("Lato2020")
        klik_regulamin = WebDriverWait(driver, 30).until(EC.element_to_be_clickable\
        ((By.XPATH, '//p[contains(text(),  "Oświadczam, że zapoznałem się z treścią")]/../span')))
        klik_regulamin.click()
        zarejestruj = WebDriverWait(driver, 30).until(EC.element_to_be_clickable\
        ((By.XPATH, '//input[@type="submit"][@class="c-btn is-primary"]')))
        zarejestruj.click()
        errors = driver.find_elements_by_xpath('//div[@id="indicatorMeter"]/div')
        visible_errors = [errors.text() for error in errors]
        print(len(visible_errors))
        self.assertEqual(len(errors),1)
        print(visible_errors[0])

if __name__=='__main__':
     unittest.main(verbosity=2)
