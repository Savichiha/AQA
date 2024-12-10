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


def test_form_submission(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='first-name']")))

    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys('Иван')
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys('Петров')
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys('Ленина, 55-3')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='e-mail']")))
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys('test@skypro.com')

    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys('+7985899998787')

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='zip-code']")))
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys('')

    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys('Москва')
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys('Россия')
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys('QA')
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys('SkyPro')

    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".alert")))

    alerts = driver.find_elements(By.CSS_SELECTOR, ".alert")

    for alert in alerts:
        if "alert-danger" in alert.get_attribute("class"):
            assert alert.is_displayed(), "Поле Zip code не подсвечено красным."
        elif "alert-success" in alert.get_attribute("class"):
            assert alert.is_displayed(), "Не все поля подсвечены зелёным."

    print("Все проверки прошли успешно!")