from appium import webdriver
from Base.Base import Base
import Page

class Search_Page_Obj(Base):
    def __init__(self,driver):
        Base.__init__(self,driver)

##点击搜索按钮
    def click_btn(self):
        self.click_serach(Page.s_b)
##点击输入框
    def input_btn(self,text):
        self.input_search(Page.s_i,text)
##点击返回按钮
    def click_ret(self):
        self.click_serach(Page.s_r)