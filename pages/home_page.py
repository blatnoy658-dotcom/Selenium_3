from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class HomePage:
    def __init__(self, driver):
        self.driver = driver

        # СТАБИЛЬНЫЕ ЛОКАТОРЫ
        self.profile_btn = (By.CSS_SELECTOR, ".header__avatar")
        self.exit_btn = (By.XPATH, "//*[@id='app']/div/div[2]/div/div/div[3]/div/div/div[2]/h3")
        self.confirm_exit_btn = (By.XPATH, "//*[@id='dialog']/div/div/div[2]/button[2]/span/span")

    def click_profile_btn(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.profile_btn)
        ).click()

    def click_exit_btn(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.exit_btn)
        ).click()

    def click_confirm_exit(self):
        WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable(self.confirm_exit_btn)
        ).click()
