#Thammy Franceily Vargas Acosta (25-0434)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time

class Test(unittest.TestCase):

    def url(self):
        link = self.driver.get("https://www.saucedemo.com/")
        return link
        
    #CONFIGURACION DE DRIVER
    def setUp(self):
        self.driver = webdriver.Chrome()

    ##TEST CASO DE PRUEBA N°1: Iniciar Sesion
    def test_01_login(self):
        self.url()

        ##Digitando el user
        self.connect = self.driver.find_element(By.NAME, 'user-name')
        self.connect.click()
        self.connect.send_keys("error_user")
        time.sleep(2)

        ##Digitando la password
        self.password = self.driver.find_element(By.NAME, 'password')
        self.password.click()
        self.password.send_keys("secret_sauce")
        time.sleep(2)

        ##Cliqueando boton de iniciar
        self.login= self.driver.find_element(By.ID, "login-button")
        self.login.submit()
        time.sleep(3)

    ##TEST CASO DE PRUEBA N°2: Agregar producto al carrito
    def test_02_seleccion_item(self):
        self.test_01_login()

        ##Cliqueando Agregar al carrito
        self.seleccionBoton = self.driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
        self.seleccionBoton.click()
        time.sleep(2)

        ##Verificacion que el boton cambio a remove
        self.estadoBoton = self.driver.find_element(By.NAME, "remove-sauce-labs-backpack").text
        assert self.estadoBoton == "Remove", "No se agrego item al carrito"

        ##Ir al carrito
        self.carrito = self.driver.find_element(By.CLASS_NAME, "shopping_cart_container")
        self.carrito.click()
        time.sleep(2)

    ##TEST CASO DE PRUEBA N°3: Finalizar Compra
    def test_03_completar_compra(self):
        self.test_02_seleccion_item()

        ##Cliqueando boton Checkout
        self.botonCheckout = self.driver.find_element(By.NAME, "checkout")
        self.botonCheckout.click()

        ##Ingresar los datos del usuario
        self.nombre = self.driver.find_element(By.ID, "first-name")
        self.nombre.send_keys("Thammy")
        
        self.apellido = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "last-name"))
        )
        self.apellido.send_keys("Vargas")
        
        self.codigoPostal =  self.driver.find_element(By.ID, "postal-code")
        self.codigoPostal.send_keys("250434")
        time.sleep(2)

        ##Cliqueando boton para continuar la compra
        self.botonContinuar = self.driver.find_element(By.NAME, "continue")
        self.botonContinuar.click()
        time.sleep(1)
        
        ##Cliqueando boton Finish para finalizar compra
        self.botonFinalizar = self.driver.find_element(By.NAME, "finish")
        self.botonFinalizar.click()


    #PARA CERRAR EL DRIVER
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
