from selenium import webdriver
from time import sleep
def get_creds(file,sep=':'):
    f = open(file,'r')
    creds = f.readline().split(sep)
    f.close()
    return [cred for cred in creds]

username,password=get_creds('.env')

mobile_emulation = { "deviceName": "iPhone X" }
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome('assets/webdrivers/chromedriver',options=chrome_options)

driver.get('https://www.instagram.com/accounts/login')

btns = driver.find_elements_by_css_selector('div div div div button')
for btn in btns:
    if btn.text == 'Accept':
        b = btn

b.click()
user_input = driver.find_element_by_name('username')
pass_input = driver.find_element_by_name('password')
submit = driver.find_element_by_css_selector('button[type=submit]')

user_input.send_keys(username)
pass_input.send_keys(password)
submit.click()

sleep(3)
onetap_btn = driver.find_element_by_css_selector('main div div div button')
onetap_btn.click()

sleep(3)
homescreen_btns = driver.find_elements_by_css_selector('div[role=dialog] button')
for btn in homescreen_btns:
    if btn.text == 'Cancel':
        hs_b = btn
hs_b.click()