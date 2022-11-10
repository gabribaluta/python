import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):
    EMAIL_INPUT = (By.XPATH, '//*[@placeholder="Enter your email"]')
    SEND_EMAIL_BTN = (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/button')
    #EMAIL_ERROR = (By.XPATH, '//*[@class="MuiFormHelperText-root MuiFormHelperText-contained MuiFormHelperText-filled"]')
    EMAIL_ERROR = (By.XPATH, '// *[ @ id = "root"] / div / div[2] / div / div[1] / div / p')


    def set_email(self, email):
        #self.wait_for_elem(*self.EMAIL_INPUT)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        time.sleep(2)

    def click_email_btn(self):
        self.driver.find_element(*self.SEND_EMAIL_BTN).click()

    def verify_error_email_msg(self):
        expected = "Please enter a valid email address!"
        actual = self.driver.find_element(*self.EMAIL_ERROR).text
        self.assertEqual(expected, actual, "Error is NOT being displayed!!!")

    def navigate_to_sign_in_page(self):
        self.driver.get('https://jules.app/sign-in')
