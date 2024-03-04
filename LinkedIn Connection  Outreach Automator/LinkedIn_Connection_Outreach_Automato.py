from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options = options)
    driver.get("https://www.linkedin.com/checkpoint/lg/login?trk=homepage-basic_sign-in-submit")
    return driver


def main(email,password,pages):
    try:
        driver = get_driver()
        
        time.sleep(2)
        username_field = driver.find_element(By.ID,value="username")
        username_field.send_keys(email)
        time.sleep(1)


        # # Locate the password field and send keys
        password_field = driver.find_element(By.ID,value="password")
        password_field.send_keys(password)
        time.sleep(1)

        login_button = driver.find_element(By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button")
        login_button.click()
        time.sleep(40)
    
        page = 0
        while(page<pages):
            
            # next_button_locator = "//button[.//span[text()='Next']]"

            
            # Find all "Connect" buttons
            connect_buttons = driver.find_elements(By.XPATH, value="//button[.//span[text()='Connect']]")

            # #     # Click each "Connect" button
            for button in connect_buttons:
                button .click()
                time.sleep(2)
                note_button = driver.find_element(By.XPATH, value="//button[.//span[text()='Send without a note']]")
                if note_button.is_enabled():
                    note_button.click()
                else:
                   dismiss_button = driver.execute_script("return document.querySelector('button[aria-label=\"dismiss\"]')")
                   dismiss_button.click()
            time.sleep(2)

            # next_button = driver.find_element(By.XPATH, "button[.//svg.//span[text()='Next ')]")
            next_button = driver.execute_script("return document.querySelector('button[aria-label=\"Next\"]')")
            next_button.click()
            time.sleep(10)
            page+=1
            print("Requests sent for : ", page)
         
            
            
               
        print("Browser closed.")
        driver.quit()

    



    except NoSuchElementException as e:
        print(f"Element not found: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")



email = "youremail@mail.com"
password = "Password"
pages = 3
main(email,password,pages)
