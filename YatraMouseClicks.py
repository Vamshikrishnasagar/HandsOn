from selenium import webdriver
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class Mouse:
    def Actions(self):
        driver = webdriver.Chrome(executable_path="C:\\browzerdrivers\\chromedriver.exe")
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        time.sleep(5)
        # right_click:-

        achange = ActionChains(driver)
        right_click = driver.find_element(By.XPATH, "//span[@class='context-menu-one btn btn-neutral']")
        achange.context_click(right_click).perform()
        time.sleep(2)

        copyele = driver.find_element(By.XPATH, "//span[normalize-space()='Copy']").click()
        time.sleep(3)

act = Mouse()
act.Actions()
