from splinter import Browser
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
with Browser('chrome') as browser:
    prob_code = input("Enter the problem code in exact format: ")
    
    url = "https://www.codechef.com/problems/" + prob_code
    browser.visit(url)

    browser.fill('name','zopq')
    browser.fill('pass','zopq1667')

    button = browser.find_by_name("op");
    # find_by_id('btnK')
    button.click()


    target_link = '/submit/' + prob_code
    #browser.find_element(By.PARTIAL_LINK_TEXT, '/submit/TEST').click()
    browser.click_link_by_partial_href('/submit/TEST')
    #browser.setFileDetector(new LocalFileDetector());
    #WebElement upload = browser.findElement(By.id("edit-sourcefile"));
    #upload.sendKeys("C:\Users\user\Desktop\code.cpp");

    #browser.attach_file('edit-sourcefile','C:\Users\user\Desktop\code.cpp')
    #button1 = browser.find_by_id("edit-sourcefile")
    #button1.click()
    #try:
    #    browser.find_by_id('edit-sourcefile').send_keys('C:\\Users\\user\\Desktop\\code\\code.cpp')
    #except:
    #    print(2+3)

    
    #active_web_element = context.browser.driver.switch_to_active_element()  
    #active_web_element.send_keys(Keys.PAGE_DOWN)
    
    #elem.send_keys("C:\\Users\\user\\Desktop\\code\\code.cpp")

    browser.attach_file('files[sourcefile]', 'C:\\Users\\user\\Desktop\\code\\code.cpp')


    button1 = browser.find_by_id("edit-submit")
    button1.click()
    time.sleep(15.4)

    browser.click_link_by_partial_href('/logout')
    
    time.sleep(3.4)
