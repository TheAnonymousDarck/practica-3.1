from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config
import time

# Deprecated
# driver = webdriver.Chrome(executable_path=config('CHROMEDRIVER_PATH'))
#

driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(20)
driver.get(config('URL_SCRAPPING'))
time.sleep(5)

state = driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/section[6]/article/div/ul/li[21]/a')
print(state.text)
state.click()

time.sleep(5)
porHora = driver.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/section/ul/li[2]/h2/a')
print(porHora.text)
porHora.click()
#driver.quit()