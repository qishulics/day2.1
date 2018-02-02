
from Page.Search_Page import Search_Page_Obj

class Page_obj():
    def __init__(self,driver):
        self.driver = driver

    def return_search(self):
        return Search_Page_Obj(self.driver)