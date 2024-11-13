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

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.TAG_NAME, "button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    zip_field_color = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
    assert zip_field_color == "rgba(248, 215, 218, 1)", "Поле Zip code не подсвечено красным"

    other_fields = [
        "first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"
    ]
    for field in other_fields:
        field_color = driver.find_element(By.NAME, field).value_of_css_property("background-color")
        assert field_color == "rgba(209, 231, 221, 1)", f"Поле {field} не подсвечено зелёным"
