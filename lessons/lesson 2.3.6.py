from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link='http://suninjuly.github.io/redirect_accept.html'

browser=webdriver.Chrome()
browser.get(link)
button1=browser.find_element(By.TAG_NAME,"button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
znachenie=browser.find_element(By.ID,"input_value").text
function=calc(znachenie)
otvet=browser.find_element(By.ID,"answer")
otvet.send_keys(function)
button2=browser.find_element(By.TAG_NAME,"button")
button2.click()
