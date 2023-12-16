from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest
from selenium.webdriver.chrome.service import Service

from Pages.MongoDB.Mongo import Mongodb

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Warehouses_Showopstate(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []

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

################### check_delivery_manager_warehouse ###################

    def test02_check_delivery_manager_warehouse(self):
        delivery = Delivery(driver=self.driver)
        delivery.enter_delivery_manager_warehouse()
        delivery.enter_delivery_manager_warehouse_kahrizak()
        delivery.enter_delivery_manager_warehouse_kahrizak_orders_in_warehouse()
        delivery.enter_delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn()
        print("وارد قسمت سفارش های موجو در انبار شد.")
        print("############################################")

################### delivery_manager_warehouse_kahrizak_check_the_goods_in_warehouse ###################

    def test03_check_delivery_manager_warehouse(self):
        delivery = Delivery(driver=self.driver)
        op = delivery.enter_delivery_manager_warehouse_kahrizak_orders_in_warehouse_tn_op()
        self.driver.back()
        delivery.enter_delivery_manager_warehouse_kahrizak_check_the_goods_in_warehouse()
        print("وارد قسمت بررسی کالا موجود در انبار شد. ")
        delivery.enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse()
        sleep(1)
        delivery.enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search("0000" + op)
        delivery.enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search_btn()
        print("############################################")


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Warehouses_Showopstate , 'Warehouses_Showopstat')
