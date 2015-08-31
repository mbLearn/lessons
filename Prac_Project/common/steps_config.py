from selenium import webdriver
from lettuce import step, world, before, after
from selenium_factory.selenium_factory import SeleniumFactory
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
import os

url = "http://www.toysrus.com//"


def get_driver():
    return driver

@before.each_scenario
def startup(scenario):

    global driver

    browser = os.environ.get('BROWSER', 'FF')
    if browser == "IE":
        capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER.copy()
        capabilities['ie.ensureCleanSession'] = True
        driver = webdriver.Ie(capabilities=capabilities)
    elif browser == "CHROME":
        driver = webdriver.Chrome()
    elif browser == "SAFARI":
        driver = webdriver.Safari()
    else:
        driver = webdriver.Firefox()

    driver.implicitly_wait(70)
    driver.set_script_timeout(50)
    driver.set_page_load_timeout(50)
    driver.get(url)


@after.each_scenario
def quit(feature):
    global driver
    driver.delete_all_cookies()
    driver.quit()

@step('Handle pop up')
def pop_up(step):
    get_driver().switch_to_alert().accept()
    time.sleep(2)

@step('Close window')
def pop_up(step):
    get_driver().close()

@step("Refresh")
def pg_f5(step):
    get_driver().refresh()

@step('Switching to new window')
def new_window_switch(step):
    get_driver().switch_to_window(driver.window_handles[-1])
    time.sleep(2)