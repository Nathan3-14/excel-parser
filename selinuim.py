# from selenium import webdriver

# driver = webdriver.Chrome()
# driver.get("https://mega.nz/#!SqoDAIZR!ctCRL6U1OlrlkA_KRagX1EgJqQAN1sw-0m9kVBcJ8L8")

# is_error = driver.find_element(by=By.Name, value="")

# driver.quit()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui

driver = webdriver.Firefox()
driver.get('https://www.google.com/')
page_url=driver.find_elements_by_xpath("//a[@class='content']")
all_title = driver.find_elements_by_class_name("title")
title = [title.text for title in all_title]
print(title)
