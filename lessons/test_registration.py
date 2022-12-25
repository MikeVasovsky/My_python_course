from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


def test_reg1(browser):
    print("\nstart test1")
    link = "http://suninjuly.github.io/registration1.html"

    browser.get(link)
    firstname=browser.find_element(By.XPATH,"//input[@placeholder='Input your first name']").send_keys("123")
    lastname=browser.find_element(By.XPATH,"//input[@placeholder='Input your last name']").send_keys("123")
    email=browser.find_element(By.XPATH,"//input[@placeholder='Input your email']").send_keys("123@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
def test_reg2(browser):
    print("\nstart test2")
    link = "http://suninjuly.github.io/registration2.html"
    browser.get(link)
    firstname = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']").send_keys("123")
    lastname = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']").send_keys("123")
    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']").send_keys("123@gmail.com")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

if __name__ == "__main__": pytest.main()