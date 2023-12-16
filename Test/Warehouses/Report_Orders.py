from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Login import LoginPage
from Pages.Warehouses.Warehouses import Warehouses
import os
import unittest

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


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

################### warehouses_china_report_orders ###################

    def test02_warehouses_china_report_orders(self):
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_china_report_the_list_of_pickuped_orders()
        warehouses.enter_warehouses_china_report_orders_check_table()
        warehouses.enter_warehouses_china_report_orders_excel_output()
        warehouses.enter_warehouses_china_report_orders_tn()
        a = warehouses.enter_warehouses_china_report_orders_table_len()
        warehouses.enter_warehouses_china_report_orders_start_date("2023/02/28")
        # warehouses.enter_warehouses_china_report_orders_end_date()
        warehouses.enter_warehouses_china_report_orders_click()
        sleep(1)
        warehouses.enter_warehouses_china_report_orders_date_btn()
        b = warehouses.enter_warehouses_china_report_orders_table_len()
        assert b > a
        print("بعد از تغییر تاریخ تعداد ردیف های جدول به درستی اضافه شد.")
        warehouses.enter_warehouses_china_report_orders_table_edit()
        warehouses.enter_warehouses_china_report_orders_table_edit_general_category()
        warehouses.enter_warehouses_china_report_orders_table_edit_general_category_option()
        warehouses.enter_warehouses_china_report_orders_table_edit_detailed_classification()
        warehouses.enter_warehouses_china_report_orders_table_edit_detailed_classification_option()
        warehouses.enter_warehouses_china_report_orders_table_edit_name("دوربین جدید")
        warehouses.enter_warehouses_china_report_orders_table_edit_name_en("new camera")
        warehouses.enter_warehouses_china_report_orders_table_edit_btn()
        warehouses.enter_warehouses_china_report_orders_table_history()
        warehouses.enter_warehouses_china_report_orders_table_history_check()

        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
