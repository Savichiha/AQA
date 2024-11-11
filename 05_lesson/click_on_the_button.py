from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")

print("Количество кнопок 'Delete':", len(delete_buttons))

driver.quit()
#fbdfbf