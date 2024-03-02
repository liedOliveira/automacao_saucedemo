import time
import pytest
from conftest import setup_teardown
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.home_page import HomePage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.sobre
class TestCT0004:
    def test_ct0004_ver_sobre(self):
        login_page = LoginPage()
        home_page = HomePage()
        base_page = BasePage()

        login_page.fazer_login("standard_user", "secret_sauce")

        time.sleep(1)
        home_page.acessar_menu()

        time.sleep(2)
        home_page.acessar_sobre()

        base_page.esperar_url_mudar()

        


