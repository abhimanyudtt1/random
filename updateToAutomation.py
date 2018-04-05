from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import *
from selenium.webdriver import ActionChains
import time


FH = open('testcase.txt','r')
testCaseList = []
for i in FH:
    testCaseList.append(i.rstrip('\n'))

FO = open('config.cfg','r')
config = {}
for line in FO :
    line = line.rstrip('\n')
    line = line.replace(' ','')
    if not line.startswith('#') and '=' in line:
        (k,v) = line.split('=')
        config[k] = v




driver = webdriver.Firefox(executable_path=config['driver'])
driver.get("http://192.168.162.9/testlink/login.php")

userName = driver.find_element_by_xpath('//*[@id="login"]')
userName.send_keys(config['user'])

passw = driver.find_element_by_css_selector('#login_div > form > p:nth-child(5) > input[type="password"]')
passw.send_keys(config['password'])

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
select.select_by_visible_text('MarketingReflex')
testSpec = driver.find_element_by_css_selector('.menu_bar > a:nth-child(3)')
testSpec.click()
time.sleep(2)


for test in testCaseList:
    driver.switch_to.default_content()
    frame = driver.find_element_by_xpath('//frame[@name="titlebar"]')
    driver.switch_to.frame(frame)
    inputField = driver.find_element_by_xpath('/html/body/div[3]/form/input[1]')
    inputField.clear()
    inputField.send_keys('%s' % test)
    driver.find_element_by_xpath('//img[@title="Search Test Case by ID"]').click()
    time.sleep(2)
    driver.switch_to.default_content()
    frame = driver.find_element_by_xpath('//frame[@name="mainframe"]')
    driver.switch_to.frame(frame)
    driver.find_element_by_css_selector('[name="edit_tc"]').click()
    time.sleep(2)

    if 'executionType' in config.keys():
        select = Select(driver.find_element_by_css_selector('[name="exec_type"]'))
        select.select_by_visible_text('%s' % config['executionType'])
    if 'tags' in config.keys():
        #ne = driver.find_element_by_xpath('//img[@alt="<<"]')
        #ne.click()
        select = Select(driver.find_element_by_css_selector('[name="from_select_box"]'))
        for tag in config['tags'].split(','):
            try :
                select.select_by_visible_text('%s' % tag)
            except NoSuchElementException :
                pass
        ne = driver.find_element_by_xpath('//img[@alt=">"]')
        ne.click()

    driver.find_element_by_css_selector('[name="do_update"').click()
    time.sleep(2)


'''
# treeframe
frame = driver.find_element_by_xpath('//frame[@name="treeframe"]')
driver.switch_to.frame(frame)
driver.find_element_by_css_selector('#expand_tree').click()
time.sleep(5)

#testCaseElements = driver.find_elements_by_css_selector('span[unselectable="on"]')
#testCaseIds = []

for test in testCaseList:
    driver.switch_to.default_content()
    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="mainframe"]'))
    driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="treeframe"]'))
    driver.find_element_by_css_selector('[name="filter_tc_id"]').clear()
    driver.find_element_by_css_selector('[name="filter_tc_id"]').send_keys(test)
    driver.find_element_by_css_selector('#doUpdateTree').click()
    time.sleep(2)
    driver.find_element_by_css_selector('#expand_tree').click()
    time.sleep(2)
    i = driver.find_elements_by_css_selector('span[unselectable="on"]')
    for ele in i :
        if ele.text.split(':')[0] == test:
            ele.location_once_scrolled_into_view
            ele.click()
            time.sleep(2)
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="mainframe"]'))
            driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="workframe"]'))

            select = Select(driver.find_element_by_css_selector('[name="exec_type"]'))
            select.select_by_visible_text('Automated')
            driver.find_element_by_css_selector('[name="do_update"').click()
            time.sleep(2)







'''
# html body div.menu_bar div form select
