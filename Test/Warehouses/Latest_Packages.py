from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Login import LoginPage
from Pages.MongoDB.Mongo import Mongodb
from Pages.Warehouses.Warehouses import Warehouses
import os
import unittest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Latest_Packages(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []

################### login_warehouses ###################

    def test01_login_warehouses(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(warehouse_id2)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل انبار دار چین شد")
        print("############################################")

################### warehouses_latest_packages_check ###################

    def test02_warehouses_latest_packages_check(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_china_latest_packages()
        warehouses.enter_warehouses_china_latest_packages_check_table()
        warehouses.enter_warehouses_china_latest_packages_show_all()
        self.driver.back()
        sleep(2)
        warehouses.enter_warehouses_china_latest_packages_click_batch()
        warehouses.enter_warehouses_china_latest_packages_check_batch()
        warehouses.enter_warehouses_china_latest_packages_exiting_warehouse_and_sending_check()
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Latest_Packages , 'Latest_Packages')
