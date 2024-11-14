import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    form_data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for name in form_data.keys():
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, name))
        )

    for name, value in form_data.items():
        element = driver.find_element(By.NAME, name)
        element.clear()  # На всякий случай очистим поле перед вводом
        element.send_keys(value)

    driver.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip-code"))
    )

    zip_field_color = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    assert zip_field_color == "rgba(248, 215, 218, 1)", "Поле Zip code не подсвечено красным"

    other_fields = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
    ]
    for field in other_fields:
        field_color = driver.find_element(By.NAME, field).value_of_css_property("background-color")
        assert field_color == "rgba(209, 231, 221, 1)", f"Поле {field} не подсвечено зелёным"
