import steps_config
from steps_config import *
from selenium import webdriver
from lettuce import step, world, before, after
import re
import random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


@step('Click the "([^"]*)" link')
def click_drop_down(step, name):
    """ Click the link specified in the feature file. Use link name as a variable"""
    link_name = get_driver().find_element_by_xpath("//div[@id = 'navbar']//a[@id = 'nav-link-shopall']/span[contains(@class, 'nav-line') and contains(text(), '%s')]" %name)
    link_name.click()

@step('Click on ([^"]+) and assert ([^"]+)')
def click_link(step, link, page):
    link_to_click = get_driver().find_element_by_xpath("//div[@class = 'categoryWrapper']/a[@class = 'mainNavLink' and text() = '%s']" %link)
    link_to_click.click()
    assert_title = get_driver().find_element_by_xpath("//div[@id = 'trus_shopByModule']//h1[text() = '%s']" %page)
    click_logo = get_driver().find_element_by_xpath("//div[@id = 'hdrLogo']/a")
    click_logo.click()
