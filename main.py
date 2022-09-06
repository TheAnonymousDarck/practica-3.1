from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from decouple import config
import time
import pandas as pd

# Deprecated
# driver = webdriver.Chrome(executable_path=config('CHROMEDRIVER_PATH'))
#

driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(20)
driver.get(config('URL_SCRAPPING'))
time.sleep(2)

driver.find_element(By.XPATH, '//*[@id="page"]/main/div[4]/div[1]/section[1]/div/ul/li[6]/a').click()
time.sleep(2)

# metodo sin input
#driver.find_element(By.XPATH, '//*[@id="main"]/div[4]/div/section[6]/article/div/ul/li[21]/a').click()
#time.sleep(5)

# metodo con input
driver.find_element(By.XPATH, '//*[@id="term"]').send_keys(config('STATE_CLIMATE'))
time.sleep(5)

driver.find_element(By.XPATH, '//*[@id="cityTable"]/div/article/section/ul/li[2]/h2/a').click()
time.sleep(3)

txt_columns = driver.find_element(By.XPATH, '//*[@id="cityTable"]/div[1]/ul')
txt_columns = txt_columns.text
#print(txt_columns)

lista = list(txt_columns.split('\n'))
todays_weather = txt_columns.split('Hoy')[0].split('\n')[1:-1]
#print(todays_weather)
print(lista)

horas=list()
temp=list()
v_viento=list()

for i in range(0,len(todays_weather),3):
    horas.append(todays_weather[i])
    temp.append(todays_weather[i+1])
    v_viento.append(todays_weather[i+2])

df = pd.DataFrame({'Horas': horas, 'Temperatura': temp, 'Velocidad_viento (Km/h)': v_viento})

print(df)
df.to_csv('tiempo_hoy.csv', index=False)

driver.quit()