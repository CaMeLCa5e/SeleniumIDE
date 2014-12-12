# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class MickyMouseHunter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://disney.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_micky_mouse_hunter(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_css_selector("span.label").click()
        driver.find_element_by_css_selector("span.spinner").click()
        driver.find_element_by_xpath("//article[@id='burger']/section[3]/div/ul/span[15]/a/div").click()
        driver.find_element_by_css_selector("span._Vyb").click()
        driver.find_element_by_link_text("Ketch-All 101-0-023 Mouse Trap, Clear Lid, Galvanized Steel").click()
        driver.find_element_by_css_selector("a.pspo-title > b").click()
        driver.find_element_by_link_text("Grainger Industrial Supply").click()
        driver.find_element_by_xpath("//img[@alt='Mouse Trap,Clear Lid,Galvanized Steel']").click()
        driver.find_element_by_xpath("(//img[@alt='Mouse Trap,Clear Lid,Galvanized Steel'])[2]").click()
        driver.find_element_by_css_selector("a.q.qs").click()
        driver.find_element_by_xpath("//ol[@id='rso']/li/ol/li[6]/div/div[2]/h3/a/em").click()
        driver.find_element_by_link_text("Shop").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_vpx=AP08ScQpFmSm; | ]]
        driver.find_element_by_id("quantityInput").clear()
        driver.find_element_by_id("quantityInput").send_keys("25")
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_vpx=AP08ScQpFmSm; | ]]
        driver.find_element_by_css_selector("#addToCart > input[type=\"image\"]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_vpx=AP08ScQpFmSm; | ]]
        driver.find_element_by_xpath("//div[@id='Header']/map/area[2]").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_vpx=AP08ScQpFmSm; | ]]
        driver.find_element_by_id("yfc_chkout").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_vpx=AP08ScQpFmSm; | ]]
        driver.find_element_by_name("eventName.cartContinueEvent").click()
        # ERROR: Caught exception [ERROR: Unsupported command [selectWindow | name=_vpx=AP08ScQpFmSm; | ]]
        driver.find_element_by_css_selector("img.regGuestSubmit").click()
    
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
