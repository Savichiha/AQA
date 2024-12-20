from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, delay):
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "input[value='5']")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    def calculate_sum(self):
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(1)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()

    def get_result(self):
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        result_text = self.driver.find_element(By.CSS_SELECTOR, ".screen").text
        return result_text