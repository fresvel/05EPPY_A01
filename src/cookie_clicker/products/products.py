from abc import ABC, abstractmethod
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class Products(ABC):
    def __init__(self, driver):
        self._driver_ = driver
        self._actions_ = ActionChains(driver)
        self.last_price = 0

    @property
    @abstractmethod
    def product_id(self):
        pass

    @property
    @abstractmethod
    def product_price_id(self):
        pass

    @property
    def product_name(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"Product: {self.product_name}\nPrice: {self.price}"
    
    @property
    def price(self):
        try:
            price_element = self._driver_.find_element(By.ID, self.product_price_id)
            price_text = self._driver_.execute_script("return arguments[0].textContent;", price_element)
            price_product=float(price_text.replace(",", ""))
            return price_product#int(self._driver_.find_element(By.ID, self.product_price_id).text)
        except Exception as e:
            print(f"Error al obtener el precio del producto {self.product_name} ", e.args)
            return self.last_price
        

    def buy(self, cookies_amout):
        try:
            product_price = float(self._driver_.find_element(By.ID, self.product_price_id).text.replace(",", ""))
            if cookies_amout >= product_price:
                product = self._driver_.find_element(By.ID, self.product_id)
                self._actions_.reset_actions()
                self._actions_.move_to_element(product)
                self._actions_.click()
                self._actions_.perform()
                print(f"Se ha comprado un/a {self.product_name}.")
                return True
            return False
        except Exception as e:
            print(f"Error al comprar {self.product_name}", e.args)
            return False
            
class Cursor (Products):
    def __init__(self, driver):
        super().__init__(driver)
    
    @property
    def product_id(self):
        return "product0"
    @property

    def product_price_id(self):
        return "productPrice0"



class Grandma(Products):
    def __init__(self, driver):
        super().__init__(driver)
    
    @property
    def product_id(self):
        return "product1"
    @property
    def product_price_id(self):
        return "productPrice1"
    
class Granja(Products):
    def __init__(self, driver):
        super().__init__(driver)
    
    @property
    def product_id(self):
        return "product2"
    @property
    def product_price_id(self):
        return "productPrice2"
    
class Mine(Products):
    def __init__(self, driver):
        super().__init__(driver)
    
    @property
    def product_id(self):
        return "product3"
    @property
    def product_price_id(self):
        return "productPrice3"
