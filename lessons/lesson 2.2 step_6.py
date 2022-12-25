from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = " http://SunInJuly.github.io/execute_script.html"
browser.get(link)
browser.execute_script("window.scrollBy(0, 120);")
x=browser.find_element(By.ID,'input_value').text
y=calc(x)
rezult=browser.find_element(By.ID,"answer")
rezult.send_keys(y)
checkbox=browser.find_element(By.ID,"robotCheckbox").click()
radiobutton=browser.find_element(By.ID,"robotsRule").click()
button = browser.find_element(By.TAG_NAME,"button")

button.click()