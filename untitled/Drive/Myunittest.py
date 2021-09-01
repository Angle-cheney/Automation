# ! user/bin/python
from selenium import webdriver # 导入webdriver包
import time
import unittest
import os

class Lucky(unittest.TestCase):

    # 定义一个保存截图函数
    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file(
            '{}/{}.png'.format(os.path.abspath(r'E:\Automation\untitled\img'), img_name))

    def setUp(self):
        self.driver = webdriver.Chrome()
        time.sleep(2)
        self.driver.get("https://alins.ele.me/")
        self.driver.maximize_window()
    def tearDown(self):
        self.driver.quit()
