import time
import pytest
from conftest import setup_teardown
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT0001:
    def test_ct0001_login_valido(self):
        # instancia os objetos a serem usados no teste
        home_page = HomePage()
        login_page = LoginPage()

        # faz login
        time.sleep(2)
        login_page.fazer_login("standard_user", "secret_sauce")

        time.sleep(2)
        # verifica se o login foi efetuado com sucesso
        home_page.verificar_login_com_sucesso()
