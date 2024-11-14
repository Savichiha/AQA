from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем драйвер
driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

    # Ждем, пока появится текст "Done!"
    WebDriverWait(driver, 30).until(
        EC.text_to_be_present_in_element((By.ID, "text"), "Done!")
    )

    # Ждем, пока количество изображений с селектором "img.img-fluid" будет >= 3
    images = WebDriverWait(driver, 30).until(
        lambda d: len(d.find_elements(By.CSS_SELECTOR, "img.img-fluid")) >= 3
    )

    # Теперь можно безопасно получить третье изображение
    third_image = driver.find_elements(By.CSS_SELECTOR, "img.img-fluid")[2]
    third_image_src = third_image.get_attribute("src")
    print("URL третьего изображения:", third_image_src)

finally:
    driver.quit()


