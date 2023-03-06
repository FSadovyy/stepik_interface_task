import time
from selenium.webdriver.common.by import By

link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_existence_add_button(browser):
    browser.get(link)
    time.sleep(30)
    WebElement = browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert WebElement, \
	f"Target element not found!"