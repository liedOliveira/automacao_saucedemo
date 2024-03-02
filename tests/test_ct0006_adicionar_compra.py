import time
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.checkout_page import CheckoutPage

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.compra
@pytest.mark.smoke
class TestCT0006:
    def test_ct0006_adicinar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()
        checkout_page = CheckoutPage()

        produto1 = "Sauce Labs Backpack"
        produto2 = "Sauce Labs Bolt T-Shirt"

        login_page.fazer_login("standard_user", "secret_sauce")
        time.sleep(3)

        home_page.adicionar_ao_carrinho(produto1)
        time.sleep(3)
        home_page.acessar_carrinho()
        
        time.sleep(3)
        carrinho_page.continuar_comprando()

        time.sleep(3)
        home_page.adicionar_ao_carrinho(produto2)

        time.sleep(3)
        home_page.acessar_carrinho()
        carrinho_page.verificar_item_carrinho_existe(produto1)
        carrinho_page.verificar_item_carrinho_existe(produto2)

        time.sleep(3)
        carrinho_page.prosseguir_para_checkout()

        time.sleep(3)
        checkout_page.realizar_checkout("Liedson","Almeida","60673790")
        
        time.sleep(3)
        checkout_page.confirmar_compra()
        
        time.sleep(3)
        checkout_page.verificar_compra_realizada()

        time.sleep(3)
        checkout_page.retornar_home()
        time.sleep(3)

