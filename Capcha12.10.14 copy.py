# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Capcha121014(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://twitter.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_capcha121014(self):
        driver = self.driver
        driver.get(self.base_url + "about:home")
        driver.find_element_by_id("searchText").clear()
        driver.find_element_by_id("searchText").send_keys("internet voting poll no captcha")
        driver.find_element_by_id("searchSubmit").click()
        driver.find_element_by_link_text("Hacking Polldaddy - Faking the Votes of the Contest Poll").click()
        driver.find_element_by_link_text("Polldaddy.com").click()
        driver.find_element_by_link_text("http://answers.polldaddy.com/vote/?va=10&pt=0&r=1&p=2189218&a=10761055&o=").click()
        driver.find_element_by_xpath("//table[@id='nav']/tbody/tr/td[3]/a/span").click()
        driver.find_element_by_xpath("//table[@id='nav']/tbody/tr/td[4]/a/span").click()
        driver.find_element_by_id("gbqfq").clear()
        driver.find_element_by_id("gbqfq").send_keys("internet voting poll no captcha make python")
        driver.find_element_by_link_text("Android push notifications (tutorial) - Server Density Blog").click()
        driver.find_element_by_xpath("//table[@id='nav']/tbody/tr/td[3]/a/span").click()
        driver.find_element_by_link_text("4chan hacker discusses the manipulation of the Time poll ...").click()
        driver.find_element_by_link_text("Top Ten Web Hacking Techniques of 2012 | WhiteHat ...").click()
        driver.find_element_by_link_text("multiple instances python").click()
        driver.find_element_by_link_text("Python creating multiple instances for a single object/class ...").click()
        driver.find_element_by_link_text("CAPTCHA Re-Riding Attack").click()
        driver.find_element_by_id("gbqfq").clear()
        driver.find_element_by_id("gbqfq").send_keys("running multiple instances python firefox")
        driver.find_element_by_link_text("How to open multiple instances of Firefox using python?").click()
    
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
