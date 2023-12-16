from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Admin.Admin import Admin
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest

from Pages.MongoDB.Mongo import Mongodb
from Pages.Warehouses.Warehouses import Warehouses

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Warehouses_Receive_Confirm_Box(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []


################### login_admin ###################

    def test01_login_admin(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_admin02)
        # login.enter_login_username("989215816049")
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل ادمین شد")
        print("############################################")

################### get_op_id ###################

    def test02_login_delivery_manager(self):
        admin = Admin(driver=self.driver)
        admin.enter_admin_batches()
        admin.enter_admin_batches_shopping_list()
        a = self.driver.find_element('xpath', "//table[@class=' table  table-striped  table-hover  sort-table ']/tbody/tr[1]/td[2]/a").text
        sleep(2)
        admin.enter_admin_batches_shopping_list_search(a)
        admin.enter_admin_batches_shopping_list_search_btn()
        admin.enter_admin_batches_shopping_list_batch()
        print("با موفقیت وارد بچ شد. ")
        print("############################################")

################### login_delivery_manager ###################

    def test03_login_delivery_manager(self):
        admin = Admin(driver=self.driver)
        op1 = admin.enter_admin_batches_shopping_list_batch_op1()
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        delivery.enter_delivery_manager_warehouse()
        delivery.enter_delivery_manager_warehouse_kahrizak()
        delivery.enter_delivery_manager_warehouse_kahrizak_receipt_confirmation()
        print("وارد قسمت تاییدیه دریافت بار شد.")
        delivery.enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse()
        delivery.enter_delivery_manager_warehouses_check_receive_confirm_box()
        delivery.enter_delivery_manager_warehouses_receive_confirm_box_scan_batches()
        delivery.enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search(op1)
        delivery.enter_delivery_manager_warehouse_kahrizak_the_goods_in_warehouse_op_search_btn()
        sleep(3)
        delivery.enter_delivery_manager_warehouses_receive_confirm_box_close_print()
        delivery.enter_delivery_manager_warehouses_receive_confirm_box_check_table()
        a = delivery.delivery_manager_warehouses_receive_confirm_box_scan_batch_op_id()
        b = "0000"+op1
        print(b)
        assert a == b
        # self.driver.back()
        print("شماره op های نمایش داده شده برابر و صحیح می باشند. ")
        print("############################################")

################### check_delivery_manager_warehouse ###################

    def test04_check_receive_confirm_box_scan_batch_tn(self):
        delivery = Delivery(driver=self.driver)
        tn = delivery.delivery_delivery_manager_warehouses_receive_confirm_box_scan_batch_tn()
        delivery.enter_delivery_manager_warehouses_receive_confirm_box_quit_search(tn)
        delivery.enter_delivery_manager_warehouses_receive_confirm_box_quit_search_btn()
        sleep(2)
        delivery.enter_delivery_manager_warehouses_receive_confirm_box_check_table_tn()
        # delivery.enter_delivery_manager_warehouses_receive_confirm_box_scan_batch_tn_time()
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Warehouses_Receive_Confirm_Box , 'Warehouses_Receive_Confirm_Box')
