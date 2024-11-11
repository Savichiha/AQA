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

    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.ID, "email").send_keys("test@skypro.com")
    driver.find_element(By.ID, "phone").send_keys("+7985899998787")
    driver.find_element(By.ID, "city").send_keys("Москва")
    driver.find_element(By.ID, "country").send_keys("Россия")
    driver.find_element(By.ID, "job-position").send_keys("QA")
    driver.find_element(By.ID, "company").send_keys("SkyPro")

    driver.find_element(By.ID, "submit").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#zip[style*='border-color: red']"))
    )

    zip_field = driver.find_element(By.ID, "zip")
    assert "border-color: red" in zip_field.get_attribute("style")

    fields_to_check = [
        "first-name", "last-name", "address", "email", "phone", "city", "country", "job-position", "company"
    ]
    for field_id in fields_to_check:
        field = driver.find_element(By.ID, field_id)
        assert "border-color: green" in field.get_attribute("style"), f"Поле {field_id} не подсвечено зелёным"

