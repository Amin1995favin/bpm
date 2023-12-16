from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert

from Locators import *
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage

import unittest


driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Login_customer_manager

    def test01_login_customer_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

################### auto_need_pick_up_order #########################

    def test02_auto_need_pick_up_order(self):
        orders_create = Orders_Create(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        sleep(.1)
        orders_create.enter_click_feather_light_content()
        tasks_list.enter_customer_manager_my_tasks()
        sleep(0.3)
        orders_create.enter_click_feather_light_content()
        tasks_list.enter_customer_manager_my_tasks_auto_need_pick_up_order()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter("")
        tasks_list.enter_customer_manager_date_filter_btn()
        tasks_list.enter_customer_manager_my_tasks_click_auto_need_pick_up_order()
        tasks_list.enter_customer_manager_my_tasks_page_auto_need_pick_up_order()

###box_pickup_check

    def test03_box_pickup_check(self):
        self.driver.maximize_window()
        box_pickup = Box_Pickup(driver=self.driver)
        # box_pickup.enter_click_cargo_pickup()
        box_pickup.enter_box_pickup_check_order()
        box_pickup.enter_box_pickup_check_internal_carriage()
        box_pickup.enter_box_pickup_sender_information()

###box_pickup_send_pickup_command

    def test04_box_pickup_send_pickup_command(self):
        box_pickup = Box_Pickup(driver=self.driver)
        box_pickup.enter_box_pickup_send_the_pickup_command()
        box_pickup.enter_box_pickup_send_the_pickup_command_error()
        box_pickup.enter_box_pickup_sender_person()
        box_pickup.enter_box_pickup_sender_person_name("ملیکا کابلی")
        sleep(1)
        box_pickup.enter_box_pickup_sender_person_option()
        box_pickup.enter_box_pickup_sender_company()
        box_pickup.enter_box_pickup_sender_company_name("ملیکا کابلی")
        sleep(1)
        box_pickup.enter_box_pickup_sender_company_option()
        box_pickup.enter_box_pickup_sender_submit()
        box_pickup.enter_box_pickup_send_the_pickup_command()
        box_pickup.enter_box_pickup_cancel_the_download_order()
        box_pickup.enter_box_pickup_send_the_pickup_command()


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
