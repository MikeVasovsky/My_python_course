from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

browser=webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")
browser.maximize_window()
one=WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
button=browser.find_element(By.TAG_NAME,"button")
button.click()
browser.execute_script("window.scrollBy(0, 100);")
x=browser.find_element(By.ID,"input_value").text
result=calc(x)
answer=browser.find_element(By.XPATH,"//body//input")
answer.send_keys(result)
submit=browser.find_element(By.XPATH,"//*[@id='solve']")
submit.click()
