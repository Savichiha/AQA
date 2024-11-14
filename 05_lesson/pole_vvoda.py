from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "/path/to/geckodriver"

driver = webdriver.Firefox(executable_path=driver_path)

driver.get("http://the-internet.herokuapp.com/inputs")

input_field = driver.find_element(By.XPATH, "//input[@type='number']")

input_field.send_keys("1000")

time.sleep(1)

input_field.clear()

input_field.send_keys("999")

time.sleep(2)

driver.quit()
