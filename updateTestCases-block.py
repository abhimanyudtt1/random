from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import time
driver = webdriver.Firefox(executable_path='/Users/abhimanyu.dutta/Downloads/geckodriver')
driver.get("http://192.168.162.9/testlink/login.php")

userName = driver.find_element_by_xpath('//*[@id="login"]')
userName.send_keys('abhimanyu.dutta')

passw = driver.find_element_by_css_selector('#login_div > form > p:nth-child(5) > input[type="password"]')
passw.send_keys('Is_it_me?3')

# #login_div > form > input[type="submit"]:nth-child(6)

login = driver.find_element_by_css_selector('#login_div > form > input[type="submit"]:nth-child(6)')
login.click()
# #login_div > form > p:nth-child(5) > input[type="password"]


time.sleep(2)
# .menu_bar > div:nth-child(6) > form:nth-child(1) > select:nth-child(1)
# 'body > div.menu_bar > div > form > select'


frame = driver.find_element_by_xpath('//frame[@name="titlebar"]')
driver.switch_to.frame(frame)
drop = driver.find_elements_by_css_selector('[name="testproject"]')[0]
select = Select(drop)
select.select_by_visible_text('Analytics Engine')

testSpec = driver.find_element_by_css_selector('.menu_bar > a:nth-child(4)')
testSpec.click()

time.sleep(2)
driver.switch_to.default_content()
frame = driver.find_element_by_xpath('//frame[@name="mainframe"]')
driver.switch_to.frame(frame)
# treeframe
frame = driver.find_element_by_xpath('//frame[@name="treeframe"]')
driver.switch_to.frame(frame)

#  Click on Expand All
driver.find_element_by_css_selector('[value="Expand tree"]').location_once_scrolled_into_view
driver.find_element_by_css_selector('[value="Expand tree"]').click()
# li.x-tree-node:nth-child(57) > div:nth-child(1) > a:nth-child(4) > span:nth-child(1) > span:nth-child(1)
#extdd-16 > img:nth-child(2)
time.sleep(2)

for k,v in elementNameHash.items():
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="mainframe"]'))
    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="treeframe"]'))
    elements = driver.find_elements_by_css_selector('a >span>span>b')
    elementNameHash = map(lambda x: (x.text, x), elements)
    elementNameHash = dict(elementNameHash)

    k1 = int(k.split('-')[-1])
    if 414<k1<423 :
        v.location_once_scrolled_into_view
        v.click()
        time.sleep(2)
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="mainframe"]'))
    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="workframe"]'))
    driver.find_element_by_css_selector('.resultBox > input[value="b"]').location_once_scrolled_into_view
    driver.find_element_by_css_selector('.resultBox > input[value="b"]').click()
    driver.find_element_by_css_selector('[value="Save execution"]').click()
    time.sleep(2)



# html body div.menu_bar div form select