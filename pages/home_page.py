import conftest
from pages.base_page import BasePage
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH, "//span[@class='title' and text()=('Products')]")
        self.item_inventario = (By.XPATH, "//*[@class='inventory_item_name ' and text()='{}']")
        self.botao_adicionar_carrinho = (By.XPATH, "//*[text()='Add to cart']")
        self.icone_carrinho = (By.CLASS_NAME, "shopping_cart_link")
        self.botao_menu = (By.ID, "react-burger-menu-btn")
        self.botao_menu_sobre = (By.ID, "about_sidebar_link")
        self.botao_deslogar = (By.ID, "logout_sidebar_link")
        self.dropdown = (By.CLASS_NAME, "product_sort_container")
        self.opcao_ativa_dropdown = (By.XPATH, "//span[@class='active_option' and text()='{}']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_ao_carrinho(self, nome_item):
        item = (self.item_inventario[0], self.item_inventario[1].format(nome_item))
        self.clicar(item)
        self.clicar(self.botao_adicionar_carrinho)

    def acessar_carrinho(self):
        self.clicar(self.icone_carrinho)

    def acessar_menu(self):
        self.clicar(self.botao_menu)

    def acessar_sobre(self):
        self.clicar(self.botao_menu_sobre)

    def deslogar(self):
        self.clicar(self.botao_deslogar)
    
    def acessar_opcao_dropdown(self, opcao_dropdown):
        lista_dropdown = Select(self.encontrar_elemento(self.dropdown))
        lista_dropdown.select_by_visible_text(opcao_dropdown)
        opcao_ativa = (self.opcao_ativa_dropdown[0], self.opcao_ativa_dropdown[1].format(opcao_dropdown))
        self.verificar_se_elemento_existe(opcao_ativa)