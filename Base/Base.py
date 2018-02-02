from selenium.webdriver.support.wait import WebDriverWait


class Base():
    def __init__(self,driver):
        self.driver = driver

    def find_element_search(self,loc,timeout=10,poll=0.5):
        return WebDriverWait(self.driver,timeout,poll).\
            until(lambda x: x.find_element(*loc))

    def click_serach(self,loc):
        self.find_element_search(loc).click()

    def input_search(self,loc,text):
        input_ele = self.find_element_search(loc)
        input_ele.clear()
        input_ele.send_keys(text)
