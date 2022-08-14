from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(x))))

def print_answer(remote: webdriver.Remote):
    alert = remote.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "button.trollface").click()

    old_window = browser.current_window_handle
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_value = int(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.CSS_SELECTOR, "input#answer").send_keys(calc(x_value))

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
