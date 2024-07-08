import logging

from selenium.webdriver.common.by import By
from base.base_driver import base_Driver
from utilities.utility import util


class search_Page(base_Driver,util):
    log= util.custom_logger(logLevel=logging.INFO)
    def __init__(self,driver):
        #as importing base class which is super
        super().__int__(driver)
        self.driver=driver

    flightSearchStop_locate= "//span[contains(text(),'1 Stop') or contains(text(),'2 Stop') or contains(text(),'Non Stop')]"
    def flifht_stops(self,stops):
        self.stop=stops
        self.waitElement_to_be_clickable(By.XPATH, f"//p[normalize-space()='{self.stop}']").click()
        elements = self.waitPresence_of_all_elements_located(By.XPATH,self.flightSearchStop_locate)
        self.scrol()
        #self.log.info("Total count of flight : ", len(elements))
        #print("Total count of flight : ", len(elements))
        self.log.info("Total count of flight :{}".format(len(elements)))
        self.forloop(elements)
