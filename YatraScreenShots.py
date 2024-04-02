from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Yatra:
    def AutoSuggest(self):
        dr = webdriver.Chrome(executable_path="C:\\browzerdrivers\\chromedriver.exe")
        dr.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        dr.maximize_window()
        time.sleep(3)
        dr.find_element(By.XPATH, "//input[@id='login-input']").send_keys("Vamshi@gmail.com")
        time.sleep(2)
        but = dr.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        but.screenshot(".\\screenshoted.png")
        but.click()
        time.sleep(2)
        dr.get_screenshot_as_file("C:\\pythonProject\\Handson\\err.png")
        dr.save_screenshot(".\\test1.png")
        time.sleep(5)

obj = Yatra()
obj.AutoSuggest()



