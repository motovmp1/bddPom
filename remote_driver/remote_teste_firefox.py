import time
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver = webdriver.Remote('http://localhost:4444/wd/hub', DesiredCapabilities.FIREFOX)
print(driver.name)
print(driver.capabilities['browserVersion'])
driver.get('http://www.google.com/')
print(driver.current_url)
time.sleep(1)  # Let the user actually see something!
driver.quit()
