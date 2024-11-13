from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = "/path/to/geckodriver"

driver = webdriver.Firefox(executable_path=driver_path)

driver.get("http://the-internet.herokuapp.com/entry_ad")

time.sleep(2)

close_button = driver.find_element(By.XPATH, "//div[@class='modal-footer']//button[contains(text(), 'Close')]")
close_button.click()

time.sleep(2)

driver.quit()
