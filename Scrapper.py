# from selenium import webdriver
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json


class Scrapper:
    def __init__(self):
        options = uc.ChromeOptions()
        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,

            # Block location prompts
            "profile.default_content_setting_values.geolocation": 2,

            # Block notification popups (like "show notifications?")
            "profile.default_content_setting_values.notifications": 2
        }
        options.add_experimental_option("prefs", prefs)
        options.add_argument("--disable-blink-features=AutomationControlled")

        self.options = options
        self.driver = None
        self.link = None
        self.data = {}

    def setLink(self, link: str):
        self.link = link

    def adOpener(self):
        if not self.link:
            raise ValueError("No link set. Use setLink() before calling adOpener().")
        self.driver = uc.Chrome(options=self.options)
        self.driver.get(self.link)
        print("Please log into Facebook if prompted.")

    def waitForLogin(self):
        try:
            WebDriverWait(self.driver, 300).until(
                EC.invisibility_of_element_located((By.ID, "login_popup_cta_form"))
            )
            print("Login popup is gone. Proceeding...")
            self.driver.minimize_window()
            # print("Please remove all the uneccesary pop ups from Google or Facebook.")
            # time.sleep(3)
        except:
            print("Timeout or popup not found. Quitting.")
            self.driver.quit()

    def scrapeDescription(self):
        print("Getting the description...")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//span[text()="See more"]'))
            ).click()
        except:
            pass  # Already expanded or not there

        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1gslohp")]//span'))
            )
            spans = self.driver.find_elements(By.XPATH, '//div[contains(@class, "xz9dl7a x4uap5 xsag5q8 xkhd6sd x126k92a")]//span')
            description = " ".join([s.text for s in spans if s.text.strip()])
            # print("Description:", description)
            self.data["description"] = description
        except Exception as e:
            print("Can't find description:", e)
            self.driver.quit()

    def scrapePrice(self):
        print("Getting the price...")
        try:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1anpbxc")]//span'))
            )
            span = self.driver.find_element(By.XPATH, '//div[contains(@class, "x1anpbxc")]//span')
            price = span.text.strip()
            # print("Price:", price)
            self.data["price"] = price
        except Exception as e:
            print("Can't find price:", e)
            self.driver.quit()

    def saveToJson(self, filename="listing.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {filename}")

    def close(self):
        time.sleep(5)
        if self.driver:
            try:
                self.driver.quit()
                print("✅ Browser closed successfully.")
            except OSError as e:
                if e.winerror == 6:
                    print("⚠️ Browser window already closed or invalid handle.")
                else:
                    print(f"⚠️ Unexpected OS error: {e}")
            except Exception as e:
                print(f"⚠️ Error closing browser: {e}")
            finally:
                self.driver.service = None
                self.driver = None  # Prevent __del__ from trying again