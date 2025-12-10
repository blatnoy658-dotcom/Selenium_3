from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class AuthPage:
    def __init__(self, driver):
        self.driver = driver

        # СТАБИЛЬНЫЕ ЛОКАТОРЫ
        self.login = (By.NAME, "phone")         # Поле телефона
        self.btn_next = (By.XPATH, "//button[@type='submit']")

        self.password = (By.NAME, "password")   # Поле пароля
        self.btn_submit = (By.XPATH, "//button[@type='submit']")

        # Активные сеансы
        self.btn_sessions = (By.XPATH, "//div[contains(@class,'sessions__item')]")
        self.btn_finish = (By.XPATH, "//*[@id='dialog']/div/div/div/div[2]/div/div[1]/div[2]/div[2]/button/span/span")

    def enter_login(self, login):
        field = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.login)
        )
        field.click()
        field.clear()
        field.send_keys(login)

    def click_btn_next(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.btn_next)
        ).click()

    def enter_password(self, password):
        field = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.password)
        )
        field.click()
        field.clear()
        field.send_keys(password)

    def click_btn_submit(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.btn_submit)
        ).click()

    def click_btn_sessions(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.btn_sessions)
        ).click()

    def click_btn_finish(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.btn_finish)
        ).click()
