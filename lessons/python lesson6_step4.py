from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link=" http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.maximize_window()
    input_name = browser.find_element(By.TAG_NAME,"input")
    input_name.send_keys("Ivan")
    input_surname = browser.find_element(By.NAME, "last_name")
    input_surname.send_keys("Petrov")
    input_city = browser.find_element(By.CLASS_NAME, "form-control.city")
    input_city.send_keys("Smolensk")
    input_country = browser.find_element(By.ID, "country")
    input_country.send_keys("Russia")
    sub_button = browser.find_element(By.XPATH, '//body/div//div[6]/button[3]')
    sub_button.click()


finally:
    time.sleep(10)
    browser.quit()