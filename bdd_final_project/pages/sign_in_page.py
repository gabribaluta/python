from selenium.webdriver.common.by import By
from time import sleep
from browser import Browser
from pages.base_page import BasePage


class SignInPage(BasePage):
    LOGIN_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/form/div/div[3]/button')
    EMAIL_INPUT = (By.XPATH, '//*[@placeholder="Enter your email"]')
    PASSWORD_INPUT = (By.XPATH, '//*[@placeholder="Enter your password"]')
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@data-test-id="forgot-password-link"]')

    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')

    # step (cea mai mica actiunea ce poate sa faca un utilizator pe pagina)
    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def click_forgot_password_link(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    # step definitoon (o agregare de pasi mici care au logica sa fie puse sub o singura funtie)
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()
        sleep(3)
