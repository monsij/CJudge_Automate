from splinter import Browser
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
with Browser('chrome') as browser:
    prob_code = input("Enter the problem code in exact format: ")
    lang = input("Enter the language of the code among C/C++/Java/Python2/Python3/PyPy")
    if lang=="C":
        l_v = "C(gcc 6.3)"
    elif lang=="C++":
        l_v = "C++14(gcc 6.3)"
    elif lang=="Java":
        l_v = "Java(HotSpot 8u112)"
    elif lang=="Python2":
        l_v = "Python(cpython 2.7.13)"
    elif lang=="Python3":
        l_v = "Python3(python  3.5)"
    elif lang=="PyPy":
        l_v = "PyPy(PyPy 2.6.0)"


    url = "https://www.codechef.com/problems/" + prob_code
    browser.visit(url)
    browser.fill('name','YOUR-CODECHEF-USERNAME')
    browser.fill('pass','YOUR-CODEDCHEF-PASSWORD')
    button = browser.find_by_name("op");
    button.click()
    #target_link = '/submit/' + prob_code
    browser.click_link_by_partial_href('/submit/' + prob_code)
    # format the file path with double slashes . For example if the path is newfolder\code.cpp write it as newfolder\\code.cpp
    browser.attach_file('files[sourcefile]', 'PATH')
    server_list = browser.find_by_id('edit-language')
    server_list.select_by_text(l_v)
    button1 = browser.find_by_id("edit-submit")
    button1.click()
    time.sleep(15.4)
    browser.click_link_by_partial_href('/logout')
    time.sleep(3.4)
