# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class PeopleSChoiceVoting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_people_s_choice_voting(self):
        driver = self.driver
        driver.get(self.base_url + "/search?q=peoples+choice+awards&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-US:official&client=firefox-a&channel=fflb")
        driver.find_element_by_link_text("People's Choice Awards: Fan Favorites in Movies, Music ...").click()
        driver.find_element_by_xpath("(//a[contains(text(),'Vote')])[2]").click()
        driver.find_element_by_xpath("//div[@id='view']/div[2]/div/div[4]/div[2]/div/div[3]/div/a[2]/div").click()
        driver.find_element_by_css_selector("button.btn.btn-next-category").click()
        driver.find_element_by_css_selector("div.categories__hover-sign").click()
        driver.find_element_by_css_selector("button.btn.btn-next-category").click()
        driver.find_element_by_css_selector("div.popup__vote_again > button.btn").click()
        driver.find_element_by_xpath("//div[@id='view']/div[2]/div/div[4]/div[2]/div/div[3]/div/a[2]/div").click()
        driver.find_element_by_css_selector("button.btn.btn-next-category").click()
        driver.find_element_by_css_selector("a.categories__hover.ng-scope").click()
        driver.find_element_by_css_selector("button.btn.btn-next-category").click()
        driver.find_element_by_css_selector("div.popup__vote_again > button.btn").click()
        driver.find_element_by_xpath("//div[@id='view']/div[2]/div/div[4]/div[2]/div/div[3]/div/a[2]/div").click()
        driver.find_element_by_css_selector("button.btn.btn-next-category").click()
        driver.find_element_by_css_selector("a.categories__hover.ng-scope").click()
        driver.find_element_by_css_selector("div.popup__vote_again > button.btn").click()
        driver.find_element_by_xpath("//div[@id='view']/div[2]/div/div[4]/div[2]/div/div[3]/div/a[2]").click()
        driver.find_element_by_css_selector("button.btn.btn-next-category").click()
        driver.find_element_by_css_selector("a.categories__hover.ng-scope").click()
        driver.find_element_by_css_selector("div.popup__vote_again > button.btn").click()
    
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
