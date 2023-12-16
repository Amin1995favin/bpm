import dpack as dpack
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert
from Locators import *
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Login import LoginPage
from Pages.MongoDB.Mongo import Mongodb
from Pages.Warehouses.Warehouses import Warehouses
import os
from pathlib import Path

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

import unittest


# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Check_Warehouses_Old(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

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
#
# ################### enter_warehouses_menu_check_element ###################
#
#     def test02_enter_warehouses_menu_check_element(self):
#         warehouses = Warehouses(driver=self.driver)
#         warehouses.enter_warehouses_menu_user_profile_click()
#         warehouses.enter_warehouses_menu_user_profile_language()
#         warehouses.enter_warehouses_menu_user_profile_language_en()
#         warehouses.enter_warehouses_menu_user_profile_btn()
#         warehouses.enter_warehouses_menu_check_element()
#         warehouses.enter_warehouses_menu_check_element_text()
#
# ################### warehouses_my_tasks_check ###################
#
#     def test03_warehouses_my_tasks_check(self):
#         warehouses = Warehouses(driver=self.driver)
#         warehouses.enter_warehouses_menu_my_tasks()
#         warehouses.enter_warehouses_my_tasks_check_element()
#         warehouses.enter_warehouses_my_tasks_orders_are_waiting_to_be_batched()
#         warehouses.enter_warehouses_my_tasks_update()
#         a = warehouses.enter_warehouses_my_tasks_orders_are_waiting_to_be_batched_number()
#         b = warehouses.enter_warehouses_my_tasks_orders_are_waiting_to_be_batched_text_table()
#         print(a)
#         print(b)
#         assert a in b
#         print("عدد نمایشی بر روی کارتابل با تعداد نمایش داده شده در جدول کارتابل برابر می باشد.")
#         print("############################################")

################### warehouses_old_check ###################

    def test04_warehouses_old_check(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_old()
        warehouses.enter_warehouses_old_check()
        a = warehouses.enter_warehouses_old_text_order_in_warehouse()
        warehouses.enter_warehouses_old_check_search_orders_in_warehouse(a)
        warehouses.enter_warehouses_old_click_order_in_warehouse()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse()
        scrolled1 = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_click_tr()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_no_batch_select()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_btn()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_close_order()
        self.driver.refresh()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_btn_red()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_red_tn()
        sleep(1)
        scrolled2 = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1)
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_click_tr()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_no_batch_select()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_remove_from_order()

        sleep(1)



    #         warehouses.enter_warehouses_menu_user_profile_click()
    #         warehouses.enter_warehouses_menu_user_profile_language()
    #         warehouses.enter_warehouses_menu_user_profile_language_en()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Check_Warehouses_Old, 'Check_Warehouses_Old')
