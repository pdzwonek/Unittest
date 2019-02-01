import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class EmailRegistration(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def open_web_page(self, browser):
        browser.get('https://www.zalando.pl/kobiety-home/')

    def open_login_panel(self, browser):
        login = browser.find_element_by_xpath('//div[@class = "z-navicat-header_navToolItem z-navicat-header_navToolItem-profile"]/a')
        login.click()

    def user_login(self, browser, user_email, user_password):
        email = browser.find_element_by_name('login.email')
        email.send_keys(user_email)

        password = browser.find_element_by_name('login.password')
        password.send_keys(user_password)

        loginBtn = browser.find_element_by_xpath('//button[@class= "z-button z-coast-reef_login_button z-button--primary z-button--button"]')
        loginBtn.click()

    def error_message(self, browser):
        expectedNotification = 'Podaj pełny adres e-mail (np. jan.kowalski@domena.pl).'

        errorMessage = browser.find_element_by_xpath('//div[@class = "z-1-notification z-1-field__notification z-1-notification--inline z-1-notification--error z-1-notification--text-small"]/span[2]')

        self.assertEqual(errorMessage.text, expectedNotification)

    def test_login_to_page(self):
        browser = self.browser

        self.open_web_page(browser)

        self.open_login_panel(browser)

        self.user_login(browser, 'niepoprawny@', 'braklogowania')

        self.error_message(browser)

    def tearDown(self):
        self.browser.quit()

if __name__ == "__main__": unittest.main()




