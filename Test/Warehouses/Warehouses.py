import dpack as dpack
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert
from Locators import *
from Pages.Clearance.My_Tasks import My_Tasks
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Financial_Manager.financial_manager import Financial_Manager
from Pages.Login import LoginPage
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


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### login_warehouses ###################

    def test30_login_warehouses(self):
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        sleep(1)
        login.enter_login_username(warehouse_id)
        sleep(.3)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل انبار دار شد")
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.1)
        print("وارد انبار چین شدید.")
        warehouses.enter_warehouses_orders_in_warehouse()
        sleep(.1)
        warehouses.enter_warehouses_orders_in_warehouse_search(" ")
        print("############################################")

    ################### warehouses_orders_in_warehouse_check ###################

    def test31_warehouses_orders_in_warehouse_check(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_order_id).text
        print(a)
        warehouses.enter_warehouses_orders_in_warehouse_search(a)
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_check_count()
        warehouses.enter_warehouses_orders_in_warehouse_check_weight()
        warehouses.enter_warehouses_orders_in_warehouse_check_allow_batching_yes()
        print("############################################")

    ################### warehouses_orders_in_warehouse_create_batch ###################

    def test32_warehouses_orders_in_warehouse_create_batch(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_order_id).text
        print(a)
        warehouses.enter_warehouses_orders_in_warehouse_search(a)
        sleep(1)
        # warehouses.enter_warehouses_orders_in_warehouse_check_count()
        # warehouses.enter_warehouses_orders_in_warehouse_check_weight()
        # warehouses.enter_warehouses_orders_in_warehouse_check_allow_batching_yes()
        # sleep(.1)
        warehouses.enter_warehouses_orders_in_warehouse_click_order_id()
        warehouses.enter_warehouses_orders_in_warehouse_click_checkbox2()
        warehouses.enter_warehouses_orders_in_warehouse_click_create_new_batch()
        sleep(1)
        # warehouses.enter_warehouses_orders_in_warehouse_assert_create_new_batch()/
        sleep(.2)
        warehouses.enter_warehouses_orders_in_warehouse_closed_tab_click_batch()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_search(a)
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_click_order_id()
        warehouses.enter_warehouses_orders_in_warehouse_click_checkbox1()
        warehouses.enter_warehouses_orders_in_warehouse_select_batch()
        ### warehouses.enter_warehouses_orders_in_warehouse_select_batch_option()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_select_batch_btn()
        # warehouses.enter_warehouses_orders_in_warehouse_assert_create_add_batch()
        warehouses.enter_warehouses_orders_in_warehouse_click_batch()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_check_form_batch()
        warehouses.enter_warehouses_orders_in_warehouse_batch_check_order1()
        warehouses.enter_warehouses_orders_in_warehouse_batch_check_order2()
        # warehouses.enter_warehouses_orders_in_warehouse_replace_name_batch()
        # warehouses.enter_warehouses_orders_in_warehouse_update_name_batch()
        warehouses.enter_warehouses_orders_in_warehouse_closed_batch()
        warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        warehouses.enter_warehouses_orders_in_warehouse_waybill_number_batch("12345")
        # warehouses.enter_warehouses_orders_in_warehouse_closed_batch()
        warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        print("باید برای خروج از انبار مقصد را تعیین کنیم.")
        warehouses.enter_warehouses_orders_in_warehouse_select_destination_batch()
        warehouses.enter_warehouses_orders_in_warehouse_select_option_destination_batch()
        warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        warehouses.enter_warehouses_orders_in_warehouse_batch_shipping_international()
        print("############################################")

    ################### Login_clearance_inquery ###################

    def test33_login_clearance(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        a = warehouses.enter_warehouses_orders_in_warehouse_batch_show_number()
        op_id1 = warehouses.enter_warehouses_orders_in_warehouse_batch_show_op_id1()
        op_id2 = warehouses.enter_warehouses_orders_in_warehouse_batch_show_op_id2()
        print(a)
        print(op_id1)
        print(op_id2)
        self.driver.get(base_url)
        my_tasks = My_Tasks(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_clearance)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد")
        my_tasks.enter_clearance_my_tasks()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch()
        my_tasks.enter_clearance_my_tasks_update()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_search(a)
        my_tasks.enter_clearance_my_tasks_search_btn()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_click_batch()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_edite()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_declared_value("100")
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_btn()
        sleep(1)
        my_tasks.enter_clearance_warehouses()
        sleep(1)
        my_tasks.enter_clearance_warehouses_psp()
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation()
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id(op_id1)
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id_btn()
        sleep(1)
        # webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
        self.driver.back()
        my_tasks.enter_clearance_warehouses_psp()
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received()
        sleep(.3)
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id(op_id1)
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id_btn()
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_check_declared_value()
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_price("110")
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_price_btn()
        sleep(2)
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_price_msg()
        print("############################################")

    ################### Login_customer_manager ###################

    def test34_login_customer_manager(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath',
                                     " //*[@id='main-content-wrapper']/section[2]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/a[1]").text
        print(a)
        self.driver.get(base_url)
        tasks_list = Tasks_list(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        sleep(.1)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(0.5)
        print("############################################")

    ################### my_tasks_op_delivery_call ###################

    def test35_my_tasks_op_delivery_call(self):
        self.driver.implicitly_wait(5)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        tasks_list = Tasks_list(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_click()
        sleep(1.5)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_text_mali_fake("این توضیحات مالی تستی می باشد.")
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_date)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_date("۱۴۰۲/۱۲/۲۰")
        sleep(.3)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_name("کاربر تست")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile("0")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile_error()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile("989124455666")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone("0")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone_error()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone("982155667788")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_delivery_type()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_delivery_type_option()
        scrolled2 = self.driver.find_element('xpath', "//button[text()=' ثبت اطلاعات']")
        sleep(.4)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        sleep(.1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location(
            "تست توضیحات عدم ثبت لوکیشن")
        sleep(.4)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        print("پیش فاکتور های سفارش فاقد صاحب پیش فاکتور ی باشند. لطفا خطاها را اصلاح کنید.")
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_closed()
        # sleep(2)
        # tasks_list.enter_customer_manager_date_filter(a)
        # tasks_list.enter_customer_manager_date_filter_btn()
        print("############################################")

    ################### my_tasks_op_delivery_call ###################

    def test36_my_tasks_op_delivery_call(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_click_order()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_text("ملیکا کابلی")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_company()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_company_text("ملیکا کابلی")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_company_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_error()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_text("ملیکا کابلی")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_confirmation()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_update_exchange()
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call()
        sleep(1)
        # tasks_list.enter_customer_manager_update_my_tasks()
        # sleep(1)
        # sleep(2)
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        print("############################################")

    #
    # ################### my_tasks_op_delivery_call_confirmation ###################
    #
    #     def test37_my_tasks_op_delivery_call_confirmation(self):
    #         self.driver.implicitly_wait(10)
    #         # scrolled = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]")
    #         # sleep(.4)
    #         # scrolled.location_once_scrolled_into_view
    #         a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
    #         print(a)
    #         tasks_list = Tasks_list(driver=self.driver)
    #         clearance_inquery = Clearance_Inquery(driver=self.driver)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_click()
    #         sleep(1)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake_option()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_text_mali_fake("این توضیحات مالی تستی می باشد.")
    #         scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_date)
    #         sleep(1)
    #         scrolled1.location_once_scrolled_into_view
    #         sleep(1)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_date("۱۴۰۲/۱۲/۲۰")
    #         sleep(.3)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_name("کاربر تست")
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile("0")
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile_error()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile("989124455666")
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone("0")
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone_error()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone("982155667788")
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_delivery_type()
    #         sleep(1)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_delivery_type_option()
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
    #         scrolled2 = self.driver.find_element('xpath', "//button[text()=' ثبت اطلاعات']")
    #         sleep(1)
    #         scrolled2.location_once_scrolled_into_view
    #         sleep(1)
    #         # self.driver.find_element('xpath', "/html/body/div[8]/div[1]/span[2]").click()
    #         # sleep(.3)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
    #         sleep(1)
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location("تست توضیحات عدم ثبت لوکیشن")
    #         tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
    #         sleep(3)
    #         clearance_inquery.enter_click_alert()
    #         sleep(3)
    #         clearance_inquery.enter_click_alert()
    #         sleep(3)
    #         clearance_inquery.enter_click_alert()
    #         # sleep(.4)
    #         # scrolled2.location_once_scrolled_into_view
    #         # sleep(1)
    #         # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
    #         # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
    #         # sleep(.4)
    #         # scrolled2.location_once_scrolled_into_view
    #         # sleep(1)
    #         # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
    #         sleep(1)
    #         # clearance_inquery.enter_click_alert()
    #         print("هماهنگی ثبت شد. ")
    #         sleep(2)
    #         clearance_inquery.enter_click_alert()
    #         print("############################################")

    ################### login_Financial_Manager ###################

    def test38_login_financial_manager(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//*[@id='dateFilter']/div/input")
        b = a.get_attribute('value')
        print(b)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        financial = Financial_Manager(driver=self.driver)
        login.enter_login_username(financial_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مالی شد. ")
        financial.enter_financial_my_tasks()
        financial.enter_financial_my_tasks_need_official_invoice()
        sleep(2)
        financial.enter_financial_update_my_tasks()
        sleep(2)
        financial.enter_financial_search(b)
        sleep(1)
        financial.enter_financial_search_btn()
        print("############################################")

    ################### my_tasks_need_official_invoice ###################

    def test39_my_tasks_need_official_invoice(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        financial = Financial_Manager(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        financial.enter_financial_my_tasks_click_need_official_invoice()
        financial.enter_financial_my_tasks_need_official_invoice_click_order()
        sleep(2)
        financial.enter_financial_my_tasks_need_official_invoice_transfer_arian()
        sleep(3)
        clearance_inquery.enter_click_alert()
        sleep(2)
        clearance_inquery.enter_click_alert()
        # financial.enter_financial_my_tasks_need_official_invoice_click_order()
        print("############################################")

    ################### login_delivery_manager ###################

    def test40_delivery_manager(self):
        self.driver.implicitly_wait(10)
        # a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        # print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        # delivery = Delivery_Manager(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        delivery.enter_my_task_delivery_manager()
        # sleep(.5)
        delivery.enter_delivery_manager_my_task_all()
        delivery.enter_delivery_manager_my_task_determine_drive()
        delivery.enter_delivery_manager_my_task_update()
        sleep(1)
        delivery.enter_delivery_manager_my_task_search("")
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()
        b = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[6]/a[1]").text
        print(b)
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive()
        sleep(1)
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive_checkbox1()
        # delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive_checkbox2()
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_receive_btn()
        self.driver.refresh()
        sleep(1)
        delivery.enter_delivery_manager_my_task_search(b)
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_check_container()
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_select_container()
        sleep(1)
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_select_container_option()
        delivery.enter_delivery_manager_my_task_determine_drive_approvals_select_container_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        print("با موفقیت راننده اختصاص داده شد. ")
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()
        print("############################################")

    ################### login_delivery ###################

    def test41_delivery(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[6]/a[1]").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
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
        delivery.enter_delivery_manager_my_task_search(a)
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()
        delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order()
        delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder()
        print("تاییدیه دریافت شده توسط راننده انجام شد. ")
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
        sleep(1)
        delivery.enter_delivery_my_task_deliver_to_customer_order_id()

        print("امضای تحویل گیرنده ثبت شد. ")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
