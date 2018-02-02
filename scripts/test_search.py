import sys, os
sys.path.append(os.getcwd())

from Base.InitDriver import init_driver
from Page.Search_Page import Search_Page_Obj
from Base.Read_Data import ret_yaml_data
import pytest
from Page.Page import Page_obj



def yaml_data():
    data_list = []
    data = ret_yaml_data("search_data").get("Search_Data")
    for i in data.keys():
        data_list.append((i, data.get(i).get("test"), data.get(i).get("expect_data")))
    return data_list


class Test_Search_Page:
    def setup_class(self):
        self.driver = init_driver()
        self.search_obj = Page_obj(self.driver).return_search()
        self.search_obj.click_btn()

    def teardown_class(self):
        self.search_obj.click_ret()
        self.driver.quit()

    @pytest.mark.parametrize("test_num,text,expect_data", yaml_data())
    def test_input_text(self,test_num,text,expect_data):
        print("用例编号：",test_num)
        self.search_obj.input_btn(text)
        self.driver.get_screenshot_as_file("./%s.png" % test_num)
        assert expect_data == 456
