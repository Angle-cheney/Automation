# ! user/bin/python
import time
from BeautifulReport import BeautifulReport
from untitled.Drive.Myunittest import Lucky
from selenium.webdriver import ActionChains

class test_Home(Lucky):

    @BeautifulReport.add_test_img('点击导航栏')
    def test_home1(self):
        """首页，点击导航栏"""
        time.sleep(3)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/span/span[1]/span").click()
        self.save_img("点击导航栏")
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/span/span[2]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/span/span[3]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/span/span[4]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/span/span[5]/span").click()
        time.sleep(2)
        self.driver.find_element_by_xpath("html/body/div[1]/div/div[1]/div[1]/img").click()
        time.sleep(3)

    @BeautifulReport.add_test_img('悬浮二级标签','点击二级标签')
    def test_home2(self):
        """点击二级标签"""
        time.sleep(3)
        self.driver.find_element_by_xpath(".//*[@id='layout-main']/div[1]/div/div[2]/div[1]/div[1]/span").click()
        time.sleep(3)
        print(self.driver.current_url)
        #窗口切换
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        self.driver.switch_to.window(windows[0])
        time.sleep(3)

        #模拟鼠标悬浮操作，鼠标悬浮一级标签，展示二级标签
        more = self.driver.find_element_by_xpath(".//*[@id='layout-main']/div[1]/div/div[2]/div[1]/div[3]/span")
        ActionChains(self.driver).move_to_element(more).perform()
        self.save_img('悬浮二级标签')
        time.sleep(3)
        #点击二级标签
        self.driver.find_element_by_xpath(".//*[@id='layout-main']/div[1]/div/div[2]/div[2]/div[1]/span").click()
        self.save_img("点击二级标签")
        time.sleep(3)



if __name__ == '__main__':
    pass