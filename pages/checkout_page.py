import conftest
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.campo_first_name = (By.ID, "first-name")
        self.campo_last_name = (By.ID, "last-name")
        self.campo_postal_code = (By.ID, "postal-code")
        self.botao_continue = (By.ID, "continue")
        self.botao_finish = (By.ID, "finish")
        self.titulo_checkout_complete = (By.XPATH, "//span[(text()='Checkout: Complete!')]")
        self.botao_home = (By.ID, "back-to-products")

    def realizar_checkout(self, primeiro_nome, ultimo_nome, cep):
        self.escrever(self.campo_first_name, primeiro_nome)
        self.escrever(self.campo_last_name, ultimo_nome)
        self.escrever(self.campo_postal_code, cep)
        self.clicar(self.botao_continue)
        
    def confirmar_compra(self):
        self.clicar(self.botao_finish)

    def verificar_compra_realizada(self):
        self.verificar_se_elemento_existe(self.titulo_checkout_complete)

    def retornar_home(self):
        self.clicar(self.botao_home)