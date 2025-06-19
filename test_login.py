from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://example.com/login")

username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login")

username.send_keys("testuser")
password.send_keys("wrongpassword")
login_button.click()

print("Test Completed")
driver.quit()