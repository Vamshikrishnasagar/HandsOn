from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class DemoJs:
    def JS(self):
        dr = webdriver.Chrome(executable_path="C:\\browzerdrivers\\chromedriver.exe")
        dr.execute_script("window.open('https://www.yatra.com/','_self')")
        dr.maximize_window()
        time.sleep(5)
        dr.find_element(By.XPATH, "//a[@title='Niyo Global']//img[@class='conta iner large-banner']").click()
        time.sleep(10)


obj = DemoJs()
obj.JS()
