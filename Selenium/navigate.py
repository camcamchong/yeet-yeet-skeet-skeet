from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()

options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

driver.get('https://bookings.ok.ubc.ca/library/admin.php')

username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")


username.send_keys("18776154")
password.send_keys("082897")

driver.find_element_by_css_selector("#logon input[type='submit'").click()


driver.get('https://bookings.ok.ubc.ca/library/edit_entry.php?area=1&room=5&hour=11&minute=0&year=2018&month=12&day=17')

driver.find_element_by_id("name").send_keys("yeet yeet skeet skeet")

driver.find_element_by_xpath("//select[@id='start_seconds']/option[@value='39600']").click()

driver.find_element_by_xpath("//select[@id='end_seconds']/option[@value='46800']").click()

driver.find_element_by_id("f_phone").send_keys("2503076081")
driver.find_element_by_id("f_email").send_keys("cameronleechong@gmail.com")

driver.find_element_by_css_selector("#main input[name='save_button'").click()
