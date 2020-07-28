import time
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
caps = options.to_capabilities()
driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          desired_capabilities=caps)
print(driver.capabilities['version'])
print(driver.name)
driver.get('http://www.google.com/')
print(driver.current_url)
time.sleep(1)  # Let the user actually see something!
driver.quit()
