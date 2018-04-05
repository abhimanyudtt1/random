import selenium.webdriver.chrome.service as service
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ActionChains
import os
import time
from selenium.common import exceptions

# os.environ['PATH'] += ':/Users/abhimanyu.dutta/Downloads/geckodriver'

chromeDriver = './chromedriver'
serv = service.Service(chromeDriver)
serv.start()
# time.sleep(5) # Let the user actually see something!
driver = webdriver.Remote(
        command_executor='http://%s:4444/wd/hub' % '127.0.0.1',
        desired_capabilities={'browserName':'chrome', 'version':'ANY', 'platform':'ANY'})

driver.get('http://192.168.162.9/testlink/login.php')


#driver = webdriver.Remote(
#   command_executor='http://127.0.0.1:4444/wd/hub',
#   desired_capabilities=DesiredCapabilities.CHROME)
