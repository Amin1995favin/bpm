from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert

from Locators import *
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage

import unittest


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

###Login_customer_manager

    def test01_login_customer_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

################### review_and_correct_order #########################

    def test02_review_and_correct_order(self):
        # a = self.driver.find_element('xpath', clearance_my_tasks_search)
        # b = a.get_attribute('value')
        # print(b)
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_to_customer()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter("")
        # tasks_list.enter_customer_manager_date_filter(b)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(0.3)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        sleep(1)
        # driver.set_window_size(480, 640)
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div/div[2]/div/div[2]/div/table/thead/tr[2]/th[8]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer()
        print("فاکتور حمل به مشتری ارسال شد. ")
        sleep(2)
        scrolled2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[9]/div[1]/a[1]")
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance_not_sent_to_the_customer()
        print("فاکتور ترخیص به مشتری ارسال شد. ")
        tasks_list.enter_customer_manager_my_tasks()
        # self.driver.refresh()
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        # tasks_list.enter_customer_manager_date_filter(b)
        tasks_list.enter_customer_manager_date_filter("")
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        scrolled3 = self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[8]/div[1]/a[1]")
        sleep(1)
        scrolled3.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_approval()
        print("فاکتور حمل توسط مشتری تایید شد. ")
        scrolled4 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[9]/div[2]/a[1]")
        sleep(1)
        scrolled4.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_no_customer_approval()
        print("فاکتور ترخیص توسط مشتری تایید شد. ")

################### auto_need_shipping #########################

    def test03_auto_need_shipping(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_auto_need_shipping()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter("")
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(0.3)
        tasks_list.enter_customer_manager_my_tasks_click_need_shipping()
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_text("12345678")
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_send()
        clearance_inquery.enter_click_alert()
        print("تعداد کاراکتر ها کمتر از 10 می باشد. ")
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_text("این توضیحات تست تاییدیه برای حمل بین الملل می باشد. ")
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_send()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
