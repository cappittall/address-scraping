import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def handle_recaptcha(driver, notify_id = "noty_layout__center"):
    """
    This function waits for the user to manually solve a CAPTCHA.
    
    Args:
    - notify_id: The ID of the element used for notifying the user about the CAPTCHA.
    """
    try:
        # Wait for the CAPTCHA iframe to appear on the page
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//iframe[@title='reCAPTCHA']"))
        )
        print("reCAPTCHA detected. Please solve it.")

        # Notify the user to solve the CAPTCHA
        user_informed = False
        start_time = time.time()
        max_duration = 300  # Maximum duration to wait for CAPTCHA to be solved (in seconds)

        while True:
            elapsed_time = time.time() - start_time
            if elapsed_time > max_duration:
                print("Timeout reached. Please check the CAPTCHA and try again.")
                break

            # Prompt the user every 30 seconds if they haven't been prompted
            if not user_informed or elapsed_time % 30 == 0:
                print(f"Please solve the reCAPTCHA. Time remaining: {max_duration - int(elapsed_time)} seconds.")
                user_informed = True

            # Wait for the user to press Enter after solving the CAPTCHA
            inpt = input("Press Enter after solving the CAPTCHA. Type 'retry' to attempt again: ").strip().lower()
            if inpt == "":
                print("CAPTCHA solved. Continuing the process...")
                break
            elif inpt == "retry":
                print("Retrying CAPTCHA...")
                user_informed = False  # Reset the flag to prompt the user again
            else:
                print("Invalid input. Please solve the CAPTCHA and press Enter.")

    except TimeoutException:
        print("Timeout while waiting for the CAPTCHA to appear.")
    except NoSuchElementException:
        print("CAPTCHA element not found on the page.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
