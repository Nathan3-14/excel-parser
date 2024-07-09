from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://mega.nz/#!SqoDAIZR!ctCRL6U1OlrlkA_KRagX1EgJqQAN1sw-0m9kVBcJ8L8")

title = driver.title
print(title)

driver.quit()
