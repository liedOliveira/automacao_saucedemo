import conftest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains, Keys

class BasePage:

    def __init__(self):
        self.driver = conftest.driver
        self.url_site_teste = ("https://www.saucedemo.com/")
        self.botao_login = (By.ID, "login-button")


    
    def encontrar_elemento(self, locator):
        return self.driver.find_element(*locator)
    
    def encontrar_elementos(self, locator):
        return self.driver.find_elements(*locator)
    
    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()

    def verificar_se_elemento_existe(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"O elemento {locator} não foi encontrado"

    def pegar_texto_elemento(self, locator):
        self.esperar_elemento_aparecer(locator)
        self.encontrar_elemento(locator).text
        
    def esperar_elemento_aparecer(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(*locator))
    
    def esperar_url_mudar(self, timeout=12):
        assert WebDriverWait(self.driver, timeout).until(EC.url_changes(self.url_site_teste)), "A url não mudou"

    def verificar_existencia_elemento(self, locator):
        assert self.encontrar_elemento(locator), f"O elemento '{locator}' não existe, mas era esperado que existisse"

    def verificar_nao_existencia_elemento(self, locator):
        assert len(self.encontrar_elementos(locator)) == 0, f"O elemento '{locator}' existe, mas era esperado que não existisse"
    
    def clique_duplo(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).double_click().perform()

    def clique_direito(self, locator):
        element = self.esperar_elemento_aparecer(locator)
        ActionChains(self.driver).context_click().perform()

    def pressionar_tecla(self, locator, key):
        elem = self.encontrar_elemento(locator)
        if key == "ENTER":
            elem.send_keys(Keys.ENTER)

        elif key == "SPACE":
            elem.send_keys(Keys.SPACE)

        elif key == "F1":
            elem.send_keys(Keys.F1)
    
    def verificar_se_deslogou(self):
        self.verificar_se_elemento_existe(self.botao_login)