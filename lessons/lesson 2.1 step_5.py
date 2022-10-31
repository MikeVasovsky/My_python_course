from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link ='https://suninjuly.github.io/math.html'

try:
    browser=webdriver.Chrome()
    browser.get(link)
    input_answer=browser.find_element(By.ID,"answer")
   #input_answer.click
    x=browser.find_element(By.ID,'input_value').text
    y=calc(x)
    input_answer.send_keys(y)
    chekbox=browser.find_element(By.ID,'robotCheckbox').click()
    radio=browser.find_element(By.ID,'robotsRule').click()
    submit=browser.find_element(By.XPATH,"//div//button")
    submit.click()
finally:
    time.sleep(10)
    browser.quit()