import logging
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from base.base_driver import base_Driver
from utilities.utility import util


class LaunchPage(base_Driver):
    log = util.custom_logger(logLevel=logging.INFO)
    def __init__(self,driver):
        super().__int__(driver)
        self.driver=driver
        #self.wait = wait
    dep_locate = "//input[@id='BE_flight_origin_city']"
    arival_locate = "//input[@id='BE_flight_arrival_city']"
    date_locate = "//input[@id='BE_flight_origin_date']"
    month_locate = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    searchBtn_locate ="BE_flight_flsearch_btn"
    infant_locate = "//div[@data-flightagegroup='infant']//span[@class='ddSpinnerPlus']"
    childCount_locate= "//div[@data-flightagegroup='child']//span[@class='ddSpinnerPlus']"
        # Providing going from location set 1
    def treval_detail(self,departure,arival,date):
        self.depart_from(departure)
        self.arrive_to(arival)
        self.dept_date(date)
        self.search()
    def depart_from(self,departure):
         dept1= self.waitElement_to_be_clickable(By.XPATH,self.dep_locate)
         dept1.click()
         self.log.info("CLICKED ON DEPART FROM")
         dept1.send_keys(departure)
         time.sleep(2)
         dept1.send_keys(Keys.ENTER)
         time.sleep(2)
        # providing going to location
    def arrive_to(self, arival):

            arrival= self.waitElement_to_be_clickable(By.XPATH,self.arival_locate)
            arrival.click()
            self.log.info("CLICKED ON ARRIVING TO")
            time.sleep(4)
            arrival.send_keys(arival)
            arrival.send_keys(Keys.ENTER)

    def dept_date(self,dt):
        self.departDt=dt
        date = self.waitElement_to_be_clickable(By.XPATH,self.date_locate)
        date.click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, f"//div[@id='monthWrapper']//tbody//td[@data-date='{self.departDt}']").click()
        self.log.info("SELECTED DEPT DATE")
        time.sleep(3)
    def catagory(self,category):
        self.cat = category
        catagory=self.driver.find_element(By.XPATH, f"//a[normalize-space()='{self.cat}']").click()

    def adult_count(self):
        self.driver.find_element(By.XPATH, "//i[@class='icon icon-angle-right arrowpassengerBox']").click()
        time.sleep(3)

    def child_count(self):
        travelChild = self.driver.find_element(By.XPATH,self.childCount_locate)
        travelChild.click()
        time.sleep(3)
    def infent_count(self):
        element=self.wait_find_element(By.XPATH, self.infant_locate)
        element.click()
        time.sleep(4)
        # click on search button
    def search(self):

        search = self.driver.find_element(By.ID, self.searchBtn_locate)
        search.click()
