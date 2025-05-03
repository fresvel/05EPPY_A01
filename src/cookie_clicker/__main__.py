import sys, json
import os, time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

from cookie_clicker.cookie_game import CookieGame
from cookie_clicker.products import Cursor, Grandma, Granja, Mine

goal = 100

## Se han creado variables para controlar cuando comprar cierto tipos de 
## productos o mejoras. Se ajustaron esos valores para alcanzar la meta en el 
## menor tiempo posible.
## Se identifica que para alcanzar la meta de 100 galletas por segundo, es necesario
## comprar hasta granjas, por lo que no se trabajaron los productos de manera global
## sino que se crearon clases de cada producto hasta granjas, que heredan de una clase
## Productos.

def init_chrome_driver():
    
    driver_path =input("Ingrese la ruta absoluta del driver o enter para cargar el driver por defecto: ")
    if not driver_path:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)
        driver_path = os.path.join(current_dir, '../chrome-linux/chrome')#"../../chrome-linux/chrome" #os.environ.get("PATH_TESTING_BROWSER") or 
        print(driver_path)
    options = webdriver.ChromeOptions()
    options.binary_location = driver_path
    driver = webdriver.Chrome(options=options)
    return driver

def init_cookie_clicker(driver):
    file_path = os.path.dirname(os.path.abspath(__file__)) 
    cookies_path = os.path.join(file_path, "data","cookies.json")

    if os.path.isfile(cookies_path):
        with open(cookies_path, "r") as file:
            cookies = json.load(file)
            for cookie in cookies:
                driver.add_cookie(dict(cookie))
        print("Cookies loaded from file.")
        driver.refresh()

    espera_explicita = WebDriverWait(driver, 1)

    try: 
        boton_aceptar_cookies = espera_explicita.until(
            EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Got it!')]"))
        )
        boton_aceptar_cookies.click()
        cookies = driver.get_cookies()
        with open(cookies_path, "w") as file:
            json.dump(cookies, file)
    except Exception as e:
        print("Error in function init_cookie_clicker:")
        print(e)

    try:
        boton_idioma = espera_explicita.until(EC.element_to_be_clickable((By.ID, "langSelect-ES")))
        boton_idioma.click()
    except NoSuchElementException:
        print("Language button not found.")
    
    try:
        espera_explicita.until(EC.element_to_be_clickable((By.ID, "bigCookie")))
    except Exception as e:
        print(f"Error waiting for the big cookie button on init_cookie_clicker: {e}")


def buy_upgrades(driver, actions):
    try:
        upgrades = driver.find_elements(By.CSS_SELECTOR, "#upgrades .upgrade.enabled")
        if upgrades:
            actions.reset_actions()
            actions.move_to_element(upgrades[0])
            actions.click()
            actions.perform()
            print("Upgrade comprado.")
            return True
    except Exception as e:
        print("Error in buy_upgrades:", e)
    return False


def main_loop(driver):

    game = CookieGame(driver)
    res=game.init_big_cookie()

    print(res)

    actions = ActionChains(driver)


    cursor= Cursor(driver)
    grandma= Grandma(driver)
    granja= Granja(driver)

    granjas_amount=0
    upgrades_amount=0

    var_cursor=5
    var_grandma=0.9 #1.2
    var_granja=0.5

    while True:

        game.click_big_cookie()
        cookies_amount, cookies_per_second = game.get_cookies_score
        if goal<cookies_per_second:
            print("Goal reached!")
            break
        
        # Prioridad 0: upgrades
        if game.buy_upgrades():
            upgrades_amount += 1
            var_grandma-=1
            var_cursor-=1
            continue
        
        # Prioridad 1: cursors
        if (cursor.price <= (grandma.price)/var_cursor):
            if (cursor.buy(cookies_amount)):
                var_cursor += 1
            continue
        
        # Prioridad 2: grandmas
        if (grandma.price <= (granja.price)/var_grandma):
            if (grandma.buy(cookies_amount)):
                var_grandma += 1
            continue

        # Prioridad 3: granjas
        if (granjas_amount <= upgrades_amount/var_granja):
            if (granja.buy(cookies_amount)):
                granjas_amount += 1
            continue


        

def main():
    print("Welcome to Cookie Clicker!")
    driver = init_chrome_driver()
    driver.get("https://orteil.dashnet.org/cookieclicker")
    init_cookie_clicker(driver)
    
    start_time = time.time()
    main_loop(driver)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Time taken to reach goal: {elapsed_time:.2f} seconds")
    time.sleep(2000)
    driver.quit()

if __name__ == "__main__":
    sys.exit(main())
