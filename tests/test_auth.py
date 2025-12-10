import time

import pytest
from selenium.common.exceptions import TimeoutException

from pages.auth_page import AuthPage
from pages.home_page import HomePage


@pytest.mark.parametrize("driver_fixture", ["driver_chrome", "driver_fire_fox"])
def test_login(driver_fixture, request):
    driver = request.getfixturevalue(driver_fixture)

    driver.get("https://my.proweb.uz/log-in?q=/home")

    auth_page = AuthPage(driver)

    # 1. Ввод телефона
    auth_page.enter_login("998977253512")
    time.sleep(1)

    # 2. ОБЯЗАТЕЛЬНО! нажать "Далее"
    auth_page.click_btn_next()
    time.sleep(1)

    # 3. Ввод пароля (элемент теперь доступен)
    auth_page.enter_password("ledmonitor12345")
    time.sleep(1)

    # 4. Войти
    auth_page.click_btn_submit()

    # 5. Закрытие активных сеансов (если появится)
    try:
        auth_page.click_btn_sessions()
        auth_page.click_btn_finish()
    except TimeoutException:
        pass

    # 6. Выход из профиля
    home_page = HomePage(driver)
    home_page.click_profile_btn()
    home_page.click_exit_btn()
    home_page.click_confirm_exit()
