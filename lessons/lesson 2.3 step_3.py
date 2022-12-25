from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

browser=webdriver.Chrome()
browser.get(link)
button=browser.find_element(By.TAG_NAME,"button")
button.click()
confirm = browser.switch_to.alert
confirm.accept()
y=browser.find_element(By.ID,"input_value").text
result=calc(y)
otvet=browser.find_element(By.ID,"answer")
otvet.send_keys(result)
button=browser.find_element(By.TAG_NAME,"button")
button.click()
