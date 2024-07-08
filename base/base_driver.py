import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class base_Driver():
    def __int__(self,driver):
         self.driver = driver

    # Going to add page scroll functionality after research (Refer video: 50)
    def scrol(self):
         self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
         time.sleep(3)
         self.driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
         time.sleep(3)

    def waitElement_to_be_clickable(self,locaterType,locaterPath):
        wait = WebDriverWait(self.driver, 30)
        element= wait.until(EC.element_to_be_clickable((locaterType,locaterPath)))
        return element 

    def wait_find_element(self,locaterType, locaterPath):
        wait = WebDriverWait(self.driver, 20)
        element= self.driver.find_element((locaterType,locaterPath))
        return element

    def waitPresence_of_all_elements_located(self,locaterType, locaterPath):
        wait = WebDriverWait(self.driver, 20)
        elements=wait.until(EC.presence_of_all_elements_located((locaterType, locaterPath)))
        return elements

