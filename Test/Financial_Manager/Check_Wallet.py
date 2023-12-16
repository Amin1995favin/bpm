import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Financial_Manager.financial_manager import Financial_Manager
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Financial_Manager.Check_Wallet import Check_Wallet
from selenium.webdriver.common.alert import Alert

import unittest

from Pages.MongoDB.Mongo import Mongodb
from Pages.Persons import Persons

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Check_Wallet(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

################### Login_customer_manager ###################

    def test01_check_wallet_check_iranian_rial(self):
        self.driver.get(base_url)
        orders_create = Orders_Create(driver=self.driver)
        check_wallet = Check_Wallet(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        persons = Persons(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(.1)
        orders_create.enter_click_orders()
        a = self.driver.find_element('xpath', check_wallet_click_order5).text
        b = re.sub(r'/...*', "", a).strip()
        c = str(b)
        print(c)
        check_wallet.enter_check_wallet_click_order5()
        all_handle1 = self.driver.window_handles
        self.driver.switch_to.window(all_handle1[1])
        sleep(2)
        d = check_wallet.enter_check_wallet_click_order5_check_iranian_rial()
        e = check_wallet.enter_check_wallet_click_order5_check_euro()
        check_wallet.enter_check_wallet_click_order5_charge()
        sleep(1)
        check_wallet.enter_check_wallet_click_order5_charge_amount("1000000")
        check_wallet.enter_check_wallet_click_order5_charge_unit()
        check_wallet.enter_check_wallet_click_order5_charge_unit_option()
        check_wallet.enter_check_wallet_click_order5_charge_account()
        check_wallet.enter_check_wallet_click_order5_charge_account_option1()
        check_wallet.enter_check_wallet_click_order5_charge_payment_type()
        check_wallet.enter_check_wallet_click_order5_charge_payment_type_option()
        check_wallet.enter_check_wallet_click_order5_charge_description("توضیحات تست")
        check_wallet.enter_check_wallet_click_order5_charge_time("۱۴۰۲/۰۲/۰۹")
        check_wallet.enter_check_wallet_click_order5_charge_payer_account("1234567890123456")
        check_wallet.enter_check_wallet_click_order5_charge_btn()
        print("درخواست شارژ حساب ثبت شد. ")
        print("############################################")

################### login_Financial_Manager ###################

        self.driver.get(base_url)
        financial = Financial_Manager(driver=self.driver)
        login.enter_login_username(financial_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مالی شد. ")
        print("############################################")
        financial.enter_financial_my_tasks()
        financial.enter_financial_my_tasks_check_new_payment()
        financial.enter_financial_update_my_tasks()
        financial.enter_financial_search(c)
        financial.enter_financial_search_btn()
        financial.enter_financial_my_tasks_check_new_payment_click()
        financial.enter_financial_my_tasks_check_new_payment_approvals()
        financial.enter_financial_my_tasks_check_new_payment_description("توضیحات تایید / عدم تایید")
        financial.enter_financial_my_tasks_check_new_payment_btn()
        sleep(2)
        print("شارژ حساب توسط مالی تایید شد.")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        print("############################################")

################### Login_customer_manager ###################

        self.driver.get(base_url)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(1)
        persons.enter_psp_search_select()
        sleep(1)
        persons.enter_psp_search_select_name(c)
        persons.enter_psp_search_select_option()
        sleep(2)
        d1 = check_wallet.enter_check_wallet_click_order5_check_iranian_rial()
        assert d1 == d+1000000
        print("مبلغ مورد نظر به درستی به کیف پول اضافه شد. ")
        print("############################################")

################### Login_customer_manager ###################

    def test02_check_wallet_check_euro(self):
        self.driver.get(base_url)
        orders_create = Orders_Create(driver=self.driver)
        check_wallet = Check_Wallet(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        persons = Persons(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(.1)
        orders_create.enter_click_orders()
        a = self.driver.find_element('xpath', check_wallet_click_order5).text
        b = re.sub(r'/...*', "", a).strip()
        c = str(b)
        print(c)
        check_wallet.enter_check_wallet_click_order5()
        all_handle1 = self.driver.window_handles
        # self.driver.switch_to.window(all_handle1[1])
        self.driver.switch_to.window(all_handle1[2])
        sleep(1)
        d = check_wallet.enter_check_wallet_click_order5_check_iranian_rial()
        e = check_wallet.enter_check_wallet_click_order5_check_euro()
        check_wallet.enter_check_wallet_click_order5_charge()
        sleep(1)
        check_wallet.enter_check_wallet_click_order5_charge_amount("100")
        check_wallet.enter_check_wallet_click_order5_charge_unit()
        check_wallet.enter_check_wallet_click_order5_charge_unit_option2()
        check_wallet.enter_check_wallet_click_order5_charge_account()
        check_wallet.enter_check_wallet_click_order5_charge_account_option2()
        check_wallet.enter_check_wallet_click_order5_charge_payment_type()
        check_wallet.enter_check_wallet_click_order5_charge_payment_type_option()
        check_wallet.enter_check_wallet_click_order5_charge_description("توضیحات تست")
        check_wallet.enter_check_wallet_click_order5_charge_time("۱۴۰۲/۰۲/۰۹")
        check_wallet.enter_check_wallet_click_order5_charge_payer_account("1234567890123456")
        check_wallet.enter_check_wallet_click_order5_charge_btn()
        print("درخواست شارژ حساب ثبت شد. ")
        print("############################################")

################### login_Financial_Manager ###################

        self.driver.get(base_url)
        financial = Financial_Manager(driver=self.driver)
        login.enter_login_username(financial_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مالی شد. ")
        print("############################################")
        financial.enter_financial_my_tasks()
        financial.enter_financial_my_tasks_check_new_payment()
        financial.enter_financial_update_my_tasks()
        financial.enter_financial_search(c)
        financial.enter_financial_search_btn()
        financial.enter_financial_my_tasks_check_new_payment_click()
        financial.enter_financial_my_tasks_check_new_payment_approvals2()
        financial.enter_financial_my_tasks_check_new_payment_description("توضیحات تایید / عدم تایید")
        financial.enter_financial_my_tasks_check_new_payment_btn()
        sleep(2)
        print("شارژ حساب توسط مالی تایید شد.")
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()

        print("############################################")

################### Login_customer_manager ###################

        self.driver.get(base_url)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(2)
        persons.enter_psp_search_select()
        sleep(1)
        persons.enter_psp_search_select_name(c)
        persons.enter_psp_search_select_option()
        sleep(2)
        d1 = check_wallet.enter_check_wallet_click_order5_check_euro()
        d1 = float(d1)
        e = float(e)
        # print(type(d1))
        # print(type(e))
        # d2 = print(type(int(d1)))
        # e = print(type(int(e)))
        # d2 = (int(d1))
        # e = (int('e'))
        assert d1 == e+100
        print("مبلغ مورد نظر به درستی به کیف پول اضافه شد. ")
        print("############################################")

################### Login_customer_manager ###################

    def test03_check_wallet_check_iranian_rial_not_add(self):
        self.driver.get(base_url)
        orders_create = Orders_Create(driver=self.driver)
        check_wallet = Check_Wallet(driver=self.driver)
        persons = Persons(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(.1)
        orders_create.enter_click_orders()
        a = self.driver.find_element('xpath', check_wallet_click_order5).text
        b = re.sub(r'/...*', "", a).strip()
        c = str(b)
        print(c)
        check_wallet.enter_check_wallet_click_order5()
        all_handle1 = self.driver.window_handles
        self.driver.switch_to.window(all_handle1[3])
        # self.driver.switch_to.window(all_handle1[1])
        sleep(1)
        d = check_wallet.enter_check_wallet_click_order5_check_iranian_rial()
        e = check_wallet.enter_check_wallet_click_order5_check_euro()
        check_wallet.enter_check_wallet_click_order5_charge()
        sleep(1)
        check_wallet.enter_check_wallet_click_order5_charge_amount("1000000")
        check_wallet.enter_check_wallet_click_order5_charge_unit()
        sleep(1)
        check_wallet.enter_check_wallet_click_order5_charge_unit_option()
        check_wallet.enter_check_wallet_click_order5_charge_account()
        sleep(1)
        check_wallet.enter_check_wallet_click_order5_charge_account_option1()
        check_wallet.enter_check_wallet_click_order5_charge_payment_type()
        sleep(1)
        check_wallet.enter_check_wallet_click_order5_charge_payment_type_option()
        check_wallet.enter_check_wallet_click_order5_charge_description("توضیحات تست")
        check_wallet.enter_check_wallet_click_order5_charge_time("۱۴۰۲/۰۲/۰۹")
        check_wallet.enter_check_wallet_click_order5_charge_payer_account("1234567890123456")
        check_wallet.enter_check_wallet_click_order5_charge_btn()
        print("درخواست شارژ حساب ثبت شد. ")
        print("############################################")

################### login_Financial_Manager ###################

        self.driver.get(base_url)
        financial = Financial_Manager(driver=self.driver)
        login.enter_login_username(financial_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مالی شد. ")
        print("############################################")
        financial.enter_financial_my_tasks()
        financial.enter_financial_my_tasks_check_new_payment()
        financial.enter_financial_update_my_tasks()
        financial.enter_financial_search(c)
        financial.enter_financial_search_btn()
        financial.enter_financial_my_tasks_check_new_payment_click()
        financial.enter_financial_my_tasks_check_new_payment_not_approvals()
        financial.enter_financial_my_tasks_check_new_payment_cancellation_reason()
        financial.enter_financial_my_tasks_check_new_payment_cancellation_reason_option()
        financial.enter_financial_my_tasks_check_new_payment_description("توضیحات تایید / عدم تایید")
        financial.enter_financial_my_tasks_check_new_payment_btn()
        sleep(2)
        print("شارژ حساب توسط مالی تایید شد.")
        print("############################################")
################### Login_customer_manager ###################

        self.driver.get(base_url)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(2)
        persons.enter_psp_search_select()
        sleep(2)
        persons.enter_psp_search_select_name(c)
        sleep(1)
        persons.enter_psp_search_select_option()
        sleep(2)
        d1 = check_wallet.enter_check_wallet_click_order5_check_iranian_rial()
        assert d1 == d
        print("مبلغ مورد نظر به درستی به کیف پول اضافه شد. ")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Check_Wallet , 'Check_Wallet')
