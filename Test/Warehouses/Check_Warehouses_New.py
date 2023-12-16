import dpack as dpack
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert
from Locators import *
from Pages.Admin.Admin import Admin
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Customer_Manager.Tasks_List import Tasks_list
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


class Test_Check_Warehouses_New(unittest.TestCase):
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
################### warehouses_my_tasks_check ###################

    def test03_warehouses_my_tasks_check(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_check_warehouses_china()
        warehouses.enter_warehouses_china_notifications()
        warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/notifications/create?place_type=customermanager&branche_id=2")
        self.driver.back()
        warehouses.enter_warehouses_china_negotiations()
        self.driver.back()
        warehouses.enter_warehouses_china_warehouse_change()
        warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/warehouses/view/140100002")
        self.driver.refresh()
        warehouses.enter_warehouses_china_going_to_the_old_warehouse()
        warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/warehouses/view/140100002?old=true")
        self.driver.back()
        warehouses.enter_warehouses_china_create_a_new_batch()
        warehouses.enter_warehouses_china_assert("http://testbpm.2ms.ir/warehouses/view/140100002")
        self.driver.refresh()
        print("############################################")

################### warehouses_old_check ###################

    def test04_warehouses_new_check(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_warehouses_orders_in_warehouse()
        a = warehouses.enter_warehouses_china_orders_in_warehouse_tn()
        warehouses.enter_warehouses_china_orders_in_warehouse_search(a)
        warehouses.enter_warehouses_china_orders_in_warehouse_click_tn()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse()
        scrolled2 = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1)
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_click_tr()
        sleep(1)
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_no_batch_select()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_btn()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_close_order()
        self.driver.refresh()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_btn_red()
        sleep(1)
        scrolled2 = self.driver.find_element('xpath', warehouses_old_check_order_goods_in_warehouse_tr1)
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_click_tr()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_no_batch_select()
        warehouses.enter_warehouses_old_check_order_goods_in_warehouse_remove_from_order()
        self.driver.refresh()

################### warehouses_old_check ###################

    def test05_warehouses_new_check(self):
        warehouses = Warehouses(driver=self.driver)
        a = warehouses.enter_warehouses_china_orders_in_warehouse_tn()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_china_search(a)
        # warehouses.enter_warehouses_china_search_btn()
        # warehouses.enter_warehouses_china_search_table_check()

################### warehouses_old_check ###################

    def test06_warehouses_new_check(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        admin = Admin(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        login.enter_login_username(account_admin02)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل ادمین شد")
        admin.enter_admin_my_task()
        admin.enter_admin_my_task_customer_manager_tab()
        admin.enter_admin_my_task_customer_manager_tab_auto_need_pick_up_order()
        sleep(1)
        admin.enter_admin_my_task_update()
        sleep(2)
        admin.enter_admin_my_task_update()
        sleep(2)
        tn = admin.enter_admin_my_task_tn()
        self.driver.get(base_url)
        login.enter_login_username(warehouse_id)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل انبار دار چین شد")
        print("############################################")
        tasks_list.enter_customer_manager_my_tasks()
        self.driver.refresh()
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.1)
        warehouses.enter_warehouses_goods_loading_list()
        warehouses.enter_warehouses_china_goods_loading_list_search_click()
        warehouses.enter_warehouses_china_goods_loading_list_search(tn)
        warehouses.enter_warehouses_china_goods_loading_list_search_btn()
        warehouses.enter_warehouses_china_goods_loading_list_search_table()
        warehouses.enter_warehouses_china_goods_loading_list_search_pickup()
        warehouses.enter_warehouses_goods_loading_list_total_qty("2")
        warehouses.enter_warehouses_goods_loading_list_total_qty_update()
        print("به قسمت افزودن کالا برای بارگیری وارد شدید.")
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2()
        sleep(1)
        # warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_list()
        scrolled1 = self.driver.find_element('xpath', "//*[@id='oppickup']/button")
        sleep(2)
        scrolled1.location_once_scrolled_into_view
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print(" برای ذخیره وارد کردن دیتا الزامی می باشد.")
        sleep(2)
        warehouses.enter_load_the_goods_without_track_number_weight("120")
        warehouses.enter_load_the_goods_without_track_number_cbm(50)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_exterior_image()
        warehouses.enter_load_the_goods_without_track_number_name_en("camera")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print(" برای ذخیره تصویر درونی کالا الزامی می باشد.")
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_internal_image()
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_no_form_print()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        sleep(1)
        print("برچسب کالا اضافه شد.")
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_list()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_data2()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_exterior_image()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_internal_image()
        sleep(0.3)
        scrolled2 = self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div/div/form/div[4]/div/label")
        sleep(.2)
        scrolled2.location_once_scrolled_into_view
        sleep(.2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_no_form_print()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print("برچسب کالا اضافه شد.")
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_check_disabled_add()
        warehouses.enter_warehouses_goods_loading_list_pickup_check_add_barcode()
        warehouses.enter_warehouses_goods_loading_list_pickup_add_warehouses()
        sleep(.1)
        warehouses.enter_warehouses_goods_loading_list_pickup_success_add()
        sleep(.1)

################### warehouses_old_check ###################

    def test07_warehouses_new_check(self):
        warehouses = Warehouses(driver=self.driver)
        self.driver.refresh()
        # warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(3)
        a = warehouses.enter_warehouses_china_goods_are_sending_to_warehouse_list_count()
        warehouses.enter_warehouses_china_goods_are_sending_to_warehouse_list()
        b = warehouses.enter_warehouses_china_goods_are_sending_to_warehouse_list_count2()
        c = warehouses.enter_warehouses_china_goods_are_sending_to_warehouse_list_count3()
        assert a == b
        assert a in c
        print("تعداد نمایش داده شده برای لیست در حال ارسال به انبار به درستی نمایش داده می شود.")

        print("تست با موفقیت به پایان رسید. ")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Check_Warehouses_New , 'Check_Warehouses_New')
