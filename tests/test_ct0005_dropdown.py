import time
import pytest
from conftest import setup_teardown
from pages.login_page import LoginPage
from pages.home_page import HomePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.dropdown
class TestCT0005:
    def test_ct0005_dropdown(self):
        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page = HomePage()
        
        login_page.fazer_login("standard_user", "secret_sauce")
        home_page.verificar_login_com_sucesso()

        time.sleep(3)
        home_page.acessar_opcao_dropdown("Price (high to low)")
        
        time.sleep(3)
        home_page.acessar_opcao_dropdown("Price (low to high)")
        
        time.sleep(3)
        home_page.acessar_opcao_dropdown("Name (Z to A)")
        
        time.sleep(3)
        home_page.acessar_opcao_dropdown("Name (A to Z)")
        time.sleep(3)
    