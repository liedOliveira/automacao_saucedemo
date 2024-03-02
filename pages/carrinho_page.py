import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CarrinhoPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.item_inventario = (By.XPATH, "//div[@class='inventory_item_name' and text()='{}']")
        self.botao_continuar_comprando = (By.ID, "continue-shopping")
        self.botao_checkout = (By.ID, "checkout")

    def verificar_item_carrinho_existe(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.verificar_se_elemento_existe(item)

    def continuar_comprando(self):
        self.clicar(self.botao_continuar_comprando)

    def prosseguir_para_checkout(self):
        self.clicar(self.botao_checkout)