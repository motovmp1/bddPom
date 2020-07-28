from behave import *
from selenium import webdriver
import time
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service

sys.path.append('/home/elsys/PycharmProjects/bddPom')

from locators import Setup


@given('Launch chrome browser')
def launch_browser(context):
    # context.driver = webdriver.Chrome(
    #    executable_path="/home/elsys/PycharmProjects/bddPom/features/drivers/chromedriver")

    options = Options()
    options.headless = True
    context.driver = webdriver.Chrome(options=options,
                                      executable_path='/home/elsys/PycharmProjects/bddPom/features/drivers/chromedriver')

    time.sleep(2)
    # context.driver.maximize_window()
    context.driver.implicitly_wait(15)


@when('open orange page')
def open_page(context):
    context.driver.get(Setup.web_page_link)


@then('verify that the logo present')
def verify_logo(context):
    context.driver.find_element_by_xpath("//div[@id='divLogo']//img")


@then('close browser')
def close_browser(context):
    time.sleep(2)
    context.driver.close()
