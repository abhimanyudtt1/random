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

testSpec = driver.find_element_by_css_selector('.menu_bar > a:nth-child(3)')
testSpec.click()

time.sleep(2)
driver.switch_to.default_content()
frame = driver.find_element_by_xpath('//frame[@name="mainframe"]')
driver.switch_to.frame(frame)
# treeframe
frame = driver.find_element_by_xpath('//frame[@name="treeframe"]')
driver.switch_to.frame(frame)
driver.find_element_by_css_selector('#extdd-13 > img:nth-child(2)').click()
time.sleep(2)
driver.find_element_by_css_selector('.x-tree-ec-icon.x-tree-elbow-end-plus').click()
#extdd-16 > img:nth-child(2)
time.sleep(2)
for i in range(96,399,3) :
    if True :
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="mainframe"]'))
        driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="treeframe"]'))
        #ActionChains(driver.find_element_by_css_selector('#extdd-%s' % i)).move_to_element().perform()
        driver.find_element_by_css_selector('#extdd-%s' % i).location_once_scrolled_into_view
        driver.find_element_by_css_selector('#extdd-%s' % i).click()
        for tag in ['Train-simrank','Train-Sessionisation','Train-DBScan','Train-ConceptExtraction','Train-Classifier'
                    'predict-E2E-Pipe','Installation','Train-E2E-Pipe']:
            if tag.lower() in driver.find_element_by_css_selector('#extdd-%s' % i).text.lower() :
                break
        time.sleep(5)
        driver.switch_to.default_content()
        driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="mainframe"]'))
        driver.switch_to.frame(driver.find_element_by_xpath('//frame[@name="workframe"]'))
        driver.find_element_by_css_selector('[name="edit_tc"]').click()

    time.sleep(3)
    # from_select_box
    select = Select(driver.find_element_by_css_selector('[name="from_select_box"]'))
    try :
        select.select_by_visible_text('%s' % tag)
    except Exception:
        print "No Problem in extdd-%s" % i
    ne = driver.find_element_by_css_selector('body > div > form > div:nth-child(10) > table > tbody > tr > td > div:nth-child(3) > div > table > tbody > tr > td:nth-child(2) > img:nth-child(3)')
    ne.click()
    driver.find_element_by_css_selector('[name="do_update"').click()
    time.sleep(5)

# html body div.menu_bar div form select