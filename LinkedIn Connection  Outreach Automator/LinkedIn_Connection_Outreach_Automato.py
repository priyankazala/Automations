from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import time

# Function to initialize and return a WebDriver instance
def get_driver():
    # Configure Chrome options
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")  # Disable infobars
    options.add_argument("start-maximized")  # Maximize window on startup
    options.add_argument("no-sandbox")  # Disable sandbox mode
    options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Exclude automation switch
    options.add_argument("disable-blink-features=AutomationControlled")  # Disable Blink features controlled by automation
    # Initialize Chrome WebDriver with configured options
    driver = webdriver.Chrome(options=options)
    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/checkpoint/lg/login?trk=homepage-basic_sign-in-submit")
    return driver

# Main function to execute the automation process
def main(email, password, pages):
    try:
        # Get WebDriver instance
        driver = get_driver()

        # Wait for 2 seconds
        time.sleep(2)
        
        # Find and fill the username field
        username_field = driver.find_element(By.ID, value="username")
        username_field.send_keys(email)
        time.sleep(1)

        # Find and fill the password field
        password_field = driver.find_element(By.ID, value="password")
        password_field.send_keys(password)
        time.sleep(1)

        # Click the login button
        login_button = driver.find_element(By.XPATH, value="/html/body/div/main/div[2]/div[1]/form/div[3]/button")
        login_button.click()
        
        # Wait for 40 seconds for login to complete
        time.sleep(40)
    
        page = 0
        # Iterate through each page
        while(page < pages):
            # Find all "Connect" buttons
            connect_buttons = driver.find_elements(By.XPATH, value="//button[.//span[text()='Connect']]")

            # Click each "Connect" button
            for button in connect_buttons:
                button.click()
                time.sleep(2)
                # Check if "Send without a note" button is enabled
                note_button = driver.find_element(By.XPATH, value="//button[.//span[text()='Send without a note']]")
                if note_button.is_enabled():
                    note_button.click()
                else:
                    # If not enabled, dismiss the connection request
                    dismiss_button = driver.execute_script("return document.querySelector('button[aria-label=\"dismiss\"]')")
                    dismiss_button.click()
                time.sleep(2)

            # Click the next button to move to the next page
            next_button = driver.execute_script("return document.querySelector('button[aria-label=\"Next\"]')")
            next_button.click()
            # Wait for 10 seconds before proceeding to the next page
            time.sleep(10)
            page += 1
            print("Requests sent for : ", page)

        # Close the browser once all pages are processed
        print("Browser closed.")
        driver.quit()

    # Handle NoSuchElementException
    except NoSuchElementException as e:
        print(f"Element not found: {e}")

    # Handle other exceptions
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
email = "youremail@mail.com"
password = "Password"
pages = 3
main(email, password, pages)
