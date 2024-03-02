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

        home_page.adicionar_ao_carrinho(produto1)
        home_page.acessar_carrinho()
        
        carrinho_page.continuar_comprando()

        home_page.adicionar_ao_carrinho(produto2)

        home_page.acessar_carrinho()
        carrinho_page.verificar_item_carrinho_existe(produto1)
        carrinho_page.verificar_item_carrinho_existe(produto2)

        carrinho_page.prosseguir_para_checkout()

        checkout_page.realizar_checkout("Liedson","Almeida","60673790")
        
        checkout_page.confirmar_compra()
        
        checkout_page.verificar_compra_realizada()

        checkout_page.retornar_home()

