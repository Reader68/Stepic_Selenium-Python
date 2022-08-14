from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try:
    browser = webdriver.Chrome()
    # говорим WebDriver ждать все элементы в течение 5 секунд
    # browser.implicitly_wait(5)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 25).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
#    print(browser.find_element(By.ID, "price").text)
    browser.find_element(By.ID, "book").click()
    
    x_value = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(calc(x_value))
    browser.find_element(By.ID, "solve").click()

    print_answer(browser)

finally:
    time.sleep(10)
    browser.quit()