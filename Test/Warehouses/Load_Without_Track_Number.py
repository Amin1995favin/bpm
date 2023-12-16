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
from Pages.Manager.Manager import Manager
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


class Test_Load_Without_Track_Number(unittest.TestCase):
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
################### load_the_goods_without_track_number_create ###################

    def test02_load_the_goods_without_track_number_create(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_china_load_the_goods_without_track_number()
        warehouses.enter_load_the_goods_without_track_number_carriage_company("favin")
        warehouses.enter_load_the_goods_without_track_number_carriage_number("1234")
        warehouses.enter_load_the_goods_without_track_number_sender_city()
        warehouses.enter_load_the_goods_without_track_number_sender_city_name("Shenzhen - China")
        warehouses.enter_load_the_goods_without_track_number_sender_city_option()
        warehouses.enter_load_the_goods_without_track_number_receiver_city()
        warehouses.enter_load_the_goods_without_track_number_receiver_city_name("tehran")
        warehouses.enter_load_the_goods_without_track_number_receiver_city_option()
        warehouses.enter_load_the_goods_without_track_number_sender_name("زهرا پیروز")
        warehouses.enter_load_the_goods_without_track_number_sender_phone("0911")
        warehouses.enter_load_the_goods_without_track_number_receiver_name("ملیکا کابلی")
        warehouses.enter_load_the_goods_without_track_number_receiver_phone("0912")
        warehouses.enter_load_the_goods_without_track_number_submit()
        print("ایجاد سفارش جدید با موفقیت انجام شد.")
        print("############################################")

################### load_the_goods_without_track_number_label ###################

    def test03_load_the_goods_without_track_number_label(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_warehouses_goods_loading_list_total_qty("1")
        warehouses.enter_warehouses_goods_loading_list_total_qty_update()
        print("به قسمت افزودن کالا برای بارگیری وارد شدید.")
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2()
        sleep(3)
        # warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_list()
        scrolled1 = self.driver.find_element('xpath', "//*[@id='oppickup']/button")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print(" برای ذخیره وارد کردن دیتا الزامی می باشد.")
        sleep(2)
        warehouses.enter_load_the_goods_without_track_number_weight("120")
        warehouses.enter_load_the_goods_without_track_number_cbm(50)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_exterior_image()
        warehouses.enter_load_the_goods_without_track_number_name_en("camera")
        sleep(1)
        # scrolled1.location_once_scrolled_into_view
        # warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        # print(" برای ذخیره تصویر درونی کالا الزامی می باشد.")
        # sleep(1)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_internal_image()
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_no_form_print()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        sleep(1)
        print("برچسب کالا اضافه شد.")
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_check_disabled_add()
        warehouses.enter_warehouses_goods_loading_list_pickup_add_warehouses()
        sleep(.1)
        warehouses.enter_warehouses_goods_loading_list_pickup_success_add()
        sleep(.1)
        print("############################################")

################### load_the_goods_without_track_number_check_order ###################

    def test04_load_the_goods_without_track_number_check_order(self):
        warehouses = Warehouses(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        sleep(1)
        warehouses.enter_load_the_goods_without_track_number_new_tn()
        orders_create.enter_product_check_color_checking_the_order()
        warehouses.enter_load_the_goods_without_track_number_check_order_shipping_cost()
        warehouses.enter_load_the_goods_without_track_number_check_order_other_inquiries()
        warehouses.enter_load_the_goods_without_track_number_check_order_invoice()
        warehouses.enter_load_the_goods_without_track_number_check_order_payment()
        warehouses.enter_load_the_goods_without_track_number_check_order_cargo_pickup()
        warehouses.enter_load_the_goods_without_track_number_check_order_loaded_goods()
        orders_create.enter_product_click_checking_the_order()
        warehouses.enter_load_the_goods_without_track_number_check_order_sender_city2()
        sleep(1)
        warehouses.enter_load_the_goods_without_track_number_check_order_receiver_city2()
        warehouses.enter_load_the_goods_without_track_number_check_order_creator2()
        warehouses.enter_load_the_goods_without_track_number_check_order_description2()
        warehouses.enter_load_the_goods_without_track_number_check_order_product_name()
        warehouses.enter_load_the_goods_without_track_number_check_order_unit_number()
        warehouses.enter_load_the_goods_without_track_number_check_order_quantity()
        warehouses.enter_load_the_goods_without_track_number_check_order_unit_weight()
        warehouses.enter_load_the_goods_without_track_number_check_order_confirm_order_details()
        # warehouses.enter_load_the_goods_without_track_number_check_order_details_of_this_order_are_approved()
        print("############################################")

################### Login_customer_manager ###################

    def test05_login_manager(self):
        self.driver.implicitly_wait(5)
        warehouses = Warehouses(driver=self.driver)
        a = warehouses.enter_load_the_goods_without_track_number_check_order_tn()
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        manager = Manager(driver=self.driver)
        login.enter_login_username(account_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر شد")
        print("############################################")
        sleep(1)
        manager.enter_click_manager_my_task()
        manager.enter_manager_my_task_all()
        manager.enter_manager_my_task_determine_the_owner_of_the_order()
        sleep(1)
        manager.enter_manager_my_task_update()
        sleep(1)
        manager.enter_manager_my_task_search(a)
        manager.enter_manager_my_task_search_btn()
        manager.enter_manager_my_task_determine_the_owner_of_the_order_click()
        manager.enter_manager_my_task_determine_the_owner_of_the_order_edite()
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_name_select()
        orders_create.enter_orders_create_name_select_text("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_name_select_option()
        print("صاحب سفارش انتخاب شد.")
        # orders_create.enter_orders_create_check_transport()
        # orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("وارد قسمت انتخاب خدمات مورد نیاز شد.")
        print("############################################")
        ################### orders_check_create_no_products ###################
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        sleep(2)
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()
        orders_create.enter_orders_create_information_approve2()
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_click_checking_the_order()

        print("############################################")

################### Login_customer_manager ###################

    def test06_login_customer_manager(self):
        self.driver.implicitly_wait(5)
        a = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[1]/h1/a[1]/span").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        sleep(1)
        orders_create.enter_menu_search()
        orders_create.enter_menu_search_name(a)
        sleep(1)
        orders_create.enter_menu_search_option()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_product_details_of_this_order_are_approved()
        sleep(2)
        orders_create.enter_product_error_details_of_this_order_are_approved()
        print("تست با موفقیت به پایان رسید. ")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Load_Without_Track_Number , 'Load_Without_Track_Number')
