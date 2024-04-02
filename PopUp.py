from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class DemoJs:
    def JS(self):
        dr = webdriver.Chrome(executable_path="C:\\browzerdrivers\\chromedriver.exe")
        dr.execute_script("window.open('https://www.yatra.com/','_self')")
        dr.maximize_window()
        time.sleep(5)
        myacct = dr.find_element(By.XPATH, "//a[contains(text(),'My Account')]")
        morebut = dr.find_element(By.XPATH, "//span[@class='more-arr']")
        achange = ActionChains(dr)
        achange.move_to_element(myacct)
        achange.move_to_element(morebut).perform()
        time.sleep(2)
        dr.find_element(By.XPATH, "//span[normalize-space()='Xplore']").click()
        time.sleep(2)


obj = DemoJs()
obj.JS()
