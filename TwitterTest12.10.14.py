# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TwitterTest1210(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://twitter.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_twitter_test1210(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_xpath("(//button[@type='submit'])[2]").click()
        driver.find_element_by_xpath("//div[@id='page-container']/div/div/div/div[3]/ul/li[3]/a/span[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[43]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[61]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[97]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[79]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[24]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        driver.find_element_by_xpath("//div[@id='page-container']/div[4]/div/div/div/div/div/div/div[4]/div/div[2]/div[2]/div[2]/a/span/b").click()
        driver.find_element_by_xpath("//div[@id='page-container']/div/div/div[2]/div/div/div[2]/div/div/ul/li[3]/a/span[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[47]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[65]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[101]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[83]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[119]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[137]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[173]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[155]").click()
        driver.find_element_by_link_text("#ArrowMidSeasonFinale").click()
        driver.find_element_by_xpath("(//button[@type='button'])[17]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[18]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[19]").click()
        driver.find_element_by_link_text("People").click()
        driver.find_element_by_xpath("(//button[@type='button'])[64]").click()
        driver.find_element_by_xpath("//li[@id='stream-item-user-349300271']/div/div[2]/div/a/strong").click()
        driver.find_element_by_xpath("//div[@id='profile_popup-body']/div/div[2]/div/div/table/tbody/tr/td[3]/a/strong").click()
        driver.find_element_by_xpath("(//button[@type='button'])[51]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[87]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[69]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[105]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[123]").click()
        driver.find_element_by_xpath("//li[@id='global-nav-home']/a/span").click()
        driver.find_element_by_xpath("(//button[@type='button'])[25]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[36]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[47]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[58]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[69]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[78]").click()
        driver.find_element_by_xpath("//div[@id='retweet-tweet-dialog-dialog']/div[2]/div[4]/button[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[89]").click()
        driver.find_element_by_xpath("//div[@id='retweet-tweet-dialog-dialog']/div[2]/div[4]/button[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[102]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[113]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[122]").click()
        driver.find_element_by_xpath("//div[@id='retweet-tweet-dialog-dialog']/div[2]/div[4]/button[2]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[135]").click()
        driver.find_element_by_id("user-dropdown-toggle").click()
        driver.find_element_by_css_selector("#signout-button > button.dropdown-link").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
