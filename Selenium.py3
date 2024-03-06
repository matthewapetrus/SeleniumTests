from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time

browser = webdriver.Chrome()
browser.get('https://orteil.dashnet.org/cookieclicker/')

browser.implicitly_wait(5)

try:
    cookieButton = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "langSelect-EN")))
    cookieButton.click()
except:
    time.sleep(5)
    browser.quit()

browser.implicitly_wait(5)

cookie_count = browser.find_element(By.ID, "cookies")
items = [browser.find_element(By. ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

for i in range(5000):
    cookie = browser.find_element(By.ID, "bigCookie")
    actions = ActionChains(browser)
    actions.click(cookie)
    actions.perform()
    count = int(cookie_count.text.split()[0])
    
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(browser)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()


time.sleep(10)
browser.quit()


"""
CLICK THROUGH LINKS

link = browser.find_element(By.LINK_TEXT, "PyCon Pakistan 2024")
link.click()

try:
    link1 = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "PyCon Pakistan 2024")))
    link1.click()

    browser.back()
    browser.back()
except:
    time.sleep(5)
    browser.quit()

time.sleep(5)
browser.quit()"""


"""""
SEARCH BAR

browser.get('https://fonts.google.com/')
assert 'Google Fonts' in browser.title
search = browser.find_element(By.ID, "mat-input-1")
search.send_keys('Cinzel' + Keys.RETURN)

try:
    main = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "catalog-results")))
    print(main.text)
    
    elements = main.find_elements(By.CLASS_NAME, "gf-tile")
    print(elements)
    for element in elements:
        header = element.find_element(By.CLASS_NAME, "tile__header")
        print(header.text)
finally:
    time.sleep(5)
    browser.quit()

time.sleep(5)
browser.quit()

input("Press Enter to continue...")
"""