# ! user/bin/python
import time
from BeautifulReport import BeautifulReport
from untitled.Drive.Myunittest import Lucky

class test_lable(Lucky):
    @BeautifulReport.add_test_img('')
    def test_Lable1(self):
        """首页，进入标签列表"""
        self.driver.maximize_window()
        self.driver.find_element_by_xpath("//span[text()='新手开店']")
        time.sleep(5)
        self.driver.find_element_by_link_text("店铺成长").click()
        self.driver.find_element_by_link_text("店铺扩张").click()

        self.driver.get_screenshot_as_file(r"C:\Users\25842\PycharmProjects\untitled\Png\test.Lable1.png")
        time.sleep(4)

if __name__ == '__main__':
    pass