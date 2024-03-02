import time
import pytest
from conftest import setup_teardown
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login_invalido
class TestCT0002:
    def test_ct0002_login_invalido(self):
        menssagem_erro_esperado = "Epic sadface: Username and password do not match any user in this service"
       
        # instancia o objeto a ser usado no teste
        login_page = LoginPage()

        # efetua o login inválido
        login_page.fazer_login("standard_user","sapopemba")
        time.sleep(2)
        # verificar se o login falhou
        login_page.verificar_menssagem_erro_login_existe()
        
        login_page.verificar_login_invalido()