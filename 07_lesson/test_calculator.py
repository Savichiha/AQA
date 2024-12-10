import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    calculator_page.set_delay(45)

    calculator_page.calculate_sum()

    result_text = calculator_page.get_result()
    print(f"Результат вычислений: {result_text}")

    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'."