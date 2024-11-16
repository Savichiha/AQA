import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    delay_input = driver.find_element(By.CSS_SELECTOR, "input[value='5']")
    delay_input.clear()
    delay_input.send_keys("45")

    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(1)").click()
    driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(2)").click()
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()

    try:

        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        print(f"Результат вычислений: {result_text}")

        assert result_text == "15", f"Expected result to be '15', but got '{result_text}'."
        print("Тест прошел успешно!")
    except Exception as e:
        print("Ошибка при ожидании результата:", str(e))
        assert False