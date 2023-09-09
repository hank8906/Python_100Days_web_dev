from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, 'fName')
lat_name = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
button = driver.find_element(By.XPATH, '/html/body/form/button')

first_name.send_keys("chun he")
lat_name.send_keys("Huang")
email.send_keys("huanghank2000@gmail.com")

button.send_keys(Keys.ENTER)

driver.quit()