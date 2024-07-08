import time
import pytest
from base.base_driver import base_Driver
from testcases.yatra_SearchPage import search_Page
from testcases.yatra_launch import LaunchPage
import softest
from ddt import ddt,data,file_data,unpack
from utilities.utility import util
@pytest.mark.usefixtures("setup")
@ddt

#class TestYatra(base_Driver):
class TestYatra(base_Driver,softest.TestCase):
    #data from XLsx file
    #@data(*util.read_data_from_excel("C:\\Users\\sheet\\PycharmProjects\\Yatra\\testdata\\inputData.xlsx", "tstdata"))
    #@pytest.fixture(autouse=True)
    #use data from csv
    @data(*util.read_data_fromm_csv("C:\\Users\\sheet\\PycharmProjects\\Yatra\\testdata\\tstdta.csv"))
    @unpack

    def test_booking(self, dept_from, going_to, date, fligt_stop):

        super().__init__()

        self.ylp= LaunchPage(self.driver)

        self.ylp.treval_detail(dept_from,going_to,date)

        #Flight stopage on search flight page
        self.ysp= search_Page(self.driver)
        self.ysp.flifht_stops(fligt_stop)



       # time.sleep(4)
