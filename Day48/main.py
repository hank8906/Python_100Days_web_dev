from selenium import webdriver
from selenium.webdriver.common.by import By

# keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
split_string = event.split('\n')

# print(split_string)

upcoming_events = {}
for i in range(0, len(split_string), 2):
    date = split_string[i]
    event_name = split_string[i + 1]

    # upcoming_events[date] = event_name

    upcoming_events[i] = {
        'time': date,
        'name': event_name
    }


print(upcoming_events)

driver.quit()