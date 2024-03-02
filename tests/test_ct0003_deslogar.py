import pytest
from conftest import setup_teardown
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.base_page import BasePage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.deslogar
class TestCT0003:
    def test_ct0003_deslogar(self):
        home_page = HomePage()
        login_page = LoginPage()
        base_page = BasePage()

        login_page.fazer_login("standard_user", "secret_sauce")
        
        home_page.acessar_menu()
        
        home_page.deslogar()
        
        base_page.verificar_se_deslogou()
