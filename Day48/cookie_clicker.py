from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# keep Chrome browser open after program finishes

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, 'cookie')
items = driver.find_elements(By.CSS_SELECTOR, '#store div')
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 7
five_min = time.time() + 60 * 5  # 5minutes

is_clicking = True

while is_clicking:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        values = []

        store = driver.find_elements(By.CSS_SELECTOR, '#store b')

        for product in store:
            product_text = product.text.strip()

            # check if product_text contains "-"
            if "-" in product_text:
                value = product_text.split('-')[1].strip()

                # ensure the value is not empty
                if value:
                    int_value = int(value.replace(",", ""))
                    values.append(int_value)
            else:
                print(f"Skipping product: {product_text}")

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(values)):
            cookie_upgrades[values[n]] = item_ids[n]

        # Get current cookie count
        money = driver.find_element(By.ID, 'money').text
        if "," in money:
            money = money.replace(",", "")
        cookie_count = int(money)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, ID in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = ID

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        # print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 7

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element(By.ID, "cps").text
        print(cookie_per_s)
        break
