import pytest
from conftest import setup_teardown
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login_invalido
class TestCT0002:
    def test_ct0002_login_invalido(self):
        login_page = LoginPage()

        login_page.fazer_login("standard_user","sapopemba")

        login_page.verificar_menssagem_erro_login_existe()
        
        login_page.verificar_login_invalido()