from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Login import LoginPage
from Pages.Warehouses.Warehouses import Warehouses
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest
import random

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### login_delivery_manager ###################

    def test01_login_delivery_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        print("############################################")

    ################### check_deliver_cars ###################

    def test02_check_deliver_cars(self):
        delivery = Delivery(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        delivery.enter_delivery_manager_warehouse()
        delivery.enter_delivery_manager_warehouse_kahrizak()
        delivery.enter_outbound_orders_from_the_warehouse()
        delivery.enter_deliver_cars_area_allocation_map()


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
