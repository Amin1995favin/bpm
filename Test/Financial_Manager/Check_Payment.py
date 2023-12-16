import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from selenium.webdriver.common.alert import Alert

import unittest

from Pages.MongoDB.Mongo import Mongodb
from Pages.Persons import Persons

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Check_Payment(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### login_delivery_manager ###################

    def test01_delivery_manager(self):
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        delivery.enter_my_task_delivery_manager()
        delivery.enter_delivery_manager_my_task_all()
        delivery.enter_delivery_my_task_deliver_to_customer()
        delivery.enter_delivery_manager_my_task_update()
        sleep(1)
        # delivery.enter_delivery_manager_my_task_search("")
        # sleep(1)
        # delivery.enter_delivery_manager_my_task_search_btn()
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        b = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[2]").text
        c = re.sub(r'/...*', "", b).strip()
        d = str(c)
        print(d)
        # d = type(c)
        # d = str(c)
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer()
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual()
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_price("20000000")
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_payment_unit()
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_payment_unit_option()
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_payment_type()
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_payment_type_option()
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_account_number("1234567899876543")
        delivery.enter_delivery_my_task_deliver_to_customer_official_residual_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        print("با موفقیت مبلغ مورد نظر ثبت شد.")
################### Login_customer_manager ###################
        self.driver.get(base_url)
        persons = Persons(driver=self.driver)
        login = LoginPage(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        login.enter_login_username(account_admin02)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل ادمین شد")
        sleep(1)
        persons.enter_psp_search_select()
        sleep(1)
        persons.enter_psp_search_select_name(c)
        persons.enter_psp_search_select_option()
        sleep(2)
        persons.enter_psp_search_show_financial()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        sleep(2)
        all_handle = self.driver.window_handles
        self.driver.switch_to.window(all_handle[1])
        sleep(2)
        self.driver.refresh()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_check_payment_by_expert()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_check_payment_by_expert_click()
        tasks_list.enter_customer_manager_my_tasks_check_payment_by_expert_accept_link()
        tasks_list.enter_customer_manager_my_tasks_check_payment_by_expert_detail("توضیحات بررسی")
        tasks_list.enter_customer_manager_my_tasks_check_payment_by_expert_btn()
        tasks_list.enter_customer_manager_my_tasks_check_payment_by_expert_presets()
        sleep(1)
        all_handle1 = self.driver.window_handles
        self.driver.switch_to.window(all_handle1[2])
        # sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_check_payment_amount1("10000000")
        # tasks_list.customer_manager_my_tasks_check_payment_amount_btn()
        # tasks_list.enter_customer_manager_my_tasks_check_payment_total_amount1_check()
        # tasks_list.enter_customer_manager_my_tasks_check_payment_amount2("10000000")
        # tasks_list.customer_manager_my_tasks_check_payment_amount_btn()
        # tasks_list.enter_customer_manager_my_tasks_check_payment_total_amount2_check()
        # sleep(2)


        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Check_Payment , 'Check_Payment')
