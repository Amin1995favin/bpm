from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Login import LoginPage
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from selenium.webdriver.common.alert import Alert

import unittest

from Pages.Persons import Persons

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

# ################### login_delivery_manager ###################
#
#     def test40_delivery_manager(self):
#         self.driver.implicitly_wait(10)
#         # a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
#         # print(a)
#         self.driver.get(base_url)
#         login = LoginPage(driver=self.driver)
#         clearance_inquery = Clearance_Inquery(driver=self.driver)
#         delivery = Delivery(driver=self.driver)
#         # delivery = Delivery_Manager(driver=self.driver)
#         login.enter_login_username(delivery_manager)
#         login.enter_login_btn_submit_next()
#         login.enter_login_password(code_no_admin)
#         login.enter_login_btn_submit()
#         print("با موفقیت وارد پنل مدیر دلیوری شد. ")
#         delivery.enter_my_task_delivery_manager()
#         # sleep(.5)
#         delivery.enter_delivery_manager_my_task_all()
#         delivery.enter_delivery_manager_my_task_determine_drive()
#         delivery.enter_delivery_manager_my_task_update()
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_search("")
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_search_btn()
#         b = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[6]/a[1]").text
#         print(b)
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive()
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive_checkbox1()
#         # delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive_checkbox2()
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive_btn()
#         self.driver.refresh()
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_search(b)
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_search_btn()
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_check_container()
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_select_container()
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_select_container_option()
#         delivery.enter_delivery_manager_my_task_determine_drive_approvals_select_container_btn()
#         sleep(1)
#         clearance_inquery.enter_click_alert()
#         sleep(1)
#         clearance_inquery.enter_click_alert()
#         print("با موفقیت راننده اختصاص داده شد. ")
#         sleep(1)
#         delivery.enter_delivery_manager_my_task_search_btn()
#         print("############################################")

################### login_delivery ###################

    def test41_delivery(self):
        self.driver.implicitly_wait(10)
        # a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[6]/a[1]").text
        # print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        # delivery = Delivery_Manager(driver=self.driver)
        login.enter_login_username(account_delivery)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل دلیوری شد. ")
        delivery.enter_my_task_delivery_manager()
        # sleep(.5)
        delivery.enter_delivery_manager_my_task_all()
        delivery.enter_delivery_my_task_deliver_to_customer()
        delivery.enter_delivery_manager_my_task_update()
        sleep(1)
        # delivery.enter_delivery_manager_my_task_search(a)
        delivery.enter_delivery_manager_my_task_search("")
        sleep(1)
        # delivery.enter_delivery_manager_my_task_search_btn()
        # delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order()
        # delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder()
        # print("تاییدیه دریافت شده توسط راننده انجام شد. ")
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer()
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file()
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
################### Login_customer_manager ###################
        self.driver.get(base_url)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        persons.enter_psp_search_select()
        persons.enter_psp_search_select_name("")
        persons.enter_psp_search_select_option()
        delivery.enter_delivery_order_delivered_assert()
        print("تست با موفقیت به پایان رسید. ")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
