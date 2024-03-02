import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message_login = (By.XPATH, "//*[@data-test='error']")
        self.titulo_home_page = (By.XPATH, "//*[@class='title' and text()='Products']")

    def fazer_login(self, usuario, senha):
        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_menssagem_erro_login_existe(self):
        self.verificar_se_elemento_existe(self.error_message_login)

    def verificar_texto_menssagem_erro(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas o texto esperado era {texto_esperado}."

    def verificar_login_invalido(self):
        self.verificar_nao_existencia_elemento(self.titulo_home_page)

