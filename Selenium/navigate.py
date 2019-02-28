from selenium import webdriver
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://bookings.ok.ubc.ca/library/admin.php')
username = driver.find_element_by_id("username")
password = driver.find_element_by_id("password")
username.send_keys("18776154")
password.send_keys("082897")
driver.find_element_by_css_selector("#logon input[type='submit'").click()
start = str(32400)
end = str(34200)
count = 1
while count < 4:
    driver.get('https://bookings.ok.ubc.ca/studyrooms/edit_entry.php?area=7&room=38&hour=11&minute=0&year=2019&month=1&day=3')
    driver.find_element_by_id("name").send_keys("yeet yeet skeet skeet")
  
  
    driver.find_element_by_xpath("//select[@id='start_seconds']/option[@value='"+start+"']").click()
    driver.find_element_by_xpath("//select[@id='end_seconds']/option[@value='"+end+"']").click()
    driver.find_element_by_id("f_phone").send_keys("2503076081")
    driver.find_element_by_id("f_email").send_keys("cameronleechong@gmail.com")
    driver.find_element_by_css_selector("#main input[name='save_button'").click()
    
    start = end
    end = str(int(end) + 1800)
    count = count +1

