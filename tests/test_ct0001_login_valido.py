import pytest
from conftest import setup_teardown
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT0001:
    def test_ct0001_login_valido(self):
        home_page = HomePage()
        login_page = LoginPage()

        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.verificar_login_com_sucesso()
