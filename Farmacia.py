import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import xmlrunner

class TestFarmaciaGeneralPaz(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.farmaciageneralpaz.com/")
        
    def test_busqueda_nivea(self):
        search_bar = self.driver.find_element(By.XPATH, "//form[@id='searchform-header']/input[@name='s']")
        search_bar.send_keys("Nivea")
        search_bar.send_keys(Keys.RETURN)
        self.assertIn("Nivea", self.driver.page_source)

    def test_busqueda_nivea2(self):
        self.driver.get("https://www.farmaciageneralpaz.com/")
        search_bar = self.driver.find_element(By.XPATH, "//form[@id='searchform-header']/input[@name='s']")
        search_bar.send_keys("Nivea")
        search_bar.send_keys(Keys.RETURN)
        self.assertIn("Nivea", self.driver.page_source)

    def test_seleccionar_producto(self):
        product_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, "Crema Corporal Nivea")
        product_link.click()
        quantity_select = self.driver.find_element(By.XPATH, "//select[contains(@class, 'qs_select')]")
        quantity_select.send_keys("3")
        add_to_cart_button = self.driver.find_element(By.XPATH, "//div[@id='variantselector-container']//form/button[1]")
        add_to_cart_button.click()
        self.assertIn("Producto añadido al carrito", self.driver.page_source)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    runner = xmlrunner.XMLTestRunner(output='test-reports')  # Configura el runner para generar el archivo XML
    unittest.main(testRunner=runner)

