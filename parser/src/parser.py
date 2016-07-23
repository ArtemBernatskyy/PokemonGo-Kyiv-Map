#coding: utf-8
import sys
import re
import os
import time
import requests
from selenium import webdriver
import math
import urllib

reload(sys)
sys.setdefaultencoding("utf-8")


# if __name__ == "__main__":

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.cache.disk.enable", False)
profile.set_preference("browser.cache.memory.enable", False)
profile.set_preference("browser.cache.offline.enable", False)
profile.set_preference("network.http.use-cache", False)

driver = webdriver.Firefox(profile)


driver.get('https://mobile.facebook.com/')
driver.find_element_by_xpath(
    '/html/body/div/div/div[3]/div/table/tbody/tr/td/div[2]/div/form/ul/li[1]/input').send_keys('tttt')
driver.find_element_by_xpath(
    '/html/body/div/div/div[3]/div/table/tbody/tr/td/div[2]/div/form/ul/li[2]/div/input').send_keys('dddd')
