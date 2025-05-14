# # from selenium import webdriver
# import undetected_chromedriver as uc
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import json


# options = uc.ChromeOptions()
# # Disable password manager
# prefs = {
#     "credentials_enable_service": False,
#     "profile.password_manager_enabled": False,

#     # Block location prompts
#     "profile.default_content_setting_values.geolocation": 2,

#     # Block notification popups (like "show notifications?")
#     "profile.default_content_setting_values.notifications": 2
# }

# options.add_experimental_option("prefs", prefs)
# options.add_argument("--disable-blink-features=AutomationControlled")
# driver = uc.Chrome(options=options)

# driver.get("https://www.facebook.com/marketplace/item/1031050451884933?ref=browse_tab&referral_code=marketplace_top_picks&referral_story_type=top_picks")
# print("A login popup will appear. Please login into your facebook.")
# try:
#     WebDriverWait(driver, 300).until(
#         EC.invisibility_of_element_located((By.ID, "login_popup_cta_form"))
#     )
#     print("Login Popup is gone. Proceeding...")
# except:
#     print("Timeout or popup not found. Quitting.")
#     driver.quit()
    

# print("Please remove all the uneccesary pop ups from google or facebook like 'save the password' or 'Location' etc.")
# time.sleep(5)
# driver.minimize_window()
# try:
#     WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.XPATH, '//span[text()="See more"]'))
#     ).click()
#     print("Clicked 'See more'")
# except:
#     print("already expanded")


# try:
#     WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1gslohp")]//span'))
#     )
#     spans = driver.find_elements(By.XPATH, '//div[contains(@class, "xz9dl7a x4uap5 xsag5q8 xkhd6sd x126k92a")]//span')
#     description = " ".join([span.text for span in spans if span.text.strip() != ""])
#     print("Description:", description)
# except:
#     print("Cant find description")
#     driver.quit()

# try:
#     WebDriverWait(driver, 20).until(
#     EC.presence_of_element_located((By.XPATH, '//div[contains(@class, "x1anpbxc")]//span'))
#     )
#     span = driver.find_element(By.XPATH, '//div[contains(@class, "x1anpbxc")]//span')
#     price = span.text.strip()
#     print("price:", price)
# except:
#     print("Cant find price")
#     driver.quit()

# data = {
#     "description" : description,
#     "price" : price,
# }
# with open("listing.json", "w", encoding="utf-8") as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# time.sleep(10)
# driver.quit()

