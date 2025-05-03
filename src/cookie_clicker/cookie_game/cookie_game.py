from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class CookieGame ():
    DEFAULT_WAIT_TIME = 200
    def __init__(self, driver, driver_time=None):
        self.__driver=driver
        self.__actions = ActionChains(driver)
        self.__espera_explicita = WebDriverWait(driver, driver_time or self.DEFAULT_WAIT_TIME)
        self.__big_cookie=None
    
    def init_big_cookie(self):     
        if self.__big_cookie is not None:
            return self.__big_cookie
        try:
            print("Waiting for the big cookie...")
            self.__big_cookie = self.__espera_explicita.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
            print("Big cookie found!")
            return True
        except Exception as e:
            print(f"Error waiting for the big cookie: {e}")
            return False
        
    def click_big_cookie(self):
        try:
            self.__actions.reset_actions()
            self.__actions.move_to_element(self.__big_cookie)
            self.__actions.click()
            self.__actions.perform()
        except Exception as e:
            print(f"Error clicking the big cookie: {e.args}")


    def buy_upgrades(self):
        try:
            upgrades = self.__driver.find_elements(By.CSS_SELECTOR, "#upgrades .upgrade.enabled")
            if upgrades:
                self.__actions.reset_actions()
                self.__actions.move_to_element(upgrades[0])
                self.__actions.click()
                self.__actions.perform()
                print("Upgrade comprado.")
                return True
        except Exception as e:
            print("Error in buy_upgrades:", e)
        return False
    
    @property
    def get_cookies_score(self):
        try: 
            cookies_string = self.__driver.find_element(By.ID, "cookies").text
            cookies_amount = int(cookies_string.split(" ")[0].replace(",", ""))
            cookies_per_second = float(cookies_string.split(" ")[-1])
            #print("Cookies:", cookies_amount, "| Goal:", cookies_per_second)
            return [cookies_amount, cookies_per_second]
        except NoSuchElementException: 
            print("Goal not found!")
            return [0, 0]
        except Exception as e:
            print("Error in check_goal:", e)
            return [0, 0]

