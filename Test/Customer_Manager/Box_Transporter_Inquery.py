from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import datetime

from Pages.Customer_Manager.Box_Transporter_Inquery import Box_Transporter_Inquery
from Pages.Login import LoginPage
from Pages.Customer_Manager.Box_Other_Service_Inquery import Box_Other_Service_Inquery
from Pages.Customer_Manager.Orders_Create import Orders_Create
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

###Login_transporter

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9020981024")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

###box_transporter_inquery_check_form

    def test02_box_transporter_inquery_check_form(self):
        orders_create = Orders_Create(driver=self.driver)
        transporter = Box_Transporter_Inquery(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id()
        transporter.enter_click_box_transporter_inquery()
        sleep(1)
        transporter.enter_box_transporter_inquery_check_table_results()
        transporter.enter_box_transporter_inquery_check_table_invoice_forwarding_factors()
        transporter.enter_box_transporter_inquery_check_table_list_of_shipping_discounts_per_kilo()
        transporter.enter_box_transporter_inquery_check_table_estimated_transportation_cost()
        transporter.enter_box_transporter_inquery_check_table_request_a_discount_on_shipping_per_kilo()
        transporter.enter_box_transporter_inquery_check_table_currency_of_invoice_shipping()
        transporter.enter_box_transporter_inquery_check_table_transportation_invoice_type()

###box_transporter_inquery_check_data

    def test03_box_transporter_inquery_check_data(self):
        transporter = Box_Transporter_Inquery(driver=self.driver)
        transporter.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        transporter.enter_box_transporter_inquery_price_unit_option()
        transporter.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        transporter.enter_box_transporter_inquery_click_the_record_is_valid()
        transporter.enter_box_transporter_inquery_per_kilo("-50000")
        transporter.enter_box_transporter_inquery_per_kilo_submit()
        transporter.enter_box_transporter_inquery_check_error_discount_per_kil()
        transporter.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        transporter.enter_box_transporter_inquery_price_unit_select()
        transporter.enter_box_transporter_inquery_price_unit_option()
        sleep(1)
        transporter.enter_box_transporter_inquery_click_the_record_is_valid()
        transporter.enter_box_transporter_inquery_per_kilo("50000")
        transporter.enter_box_transporter_inquery_per_kilo_submit()
        now = datetime.now()
        transporter.enter_box_transporter_inquery_check_is_it_valid()
        transporter.enter_box_transporter_inquery_check_the_record_is_valid()
        transporter.enter_box_transporter_inquery_check_awaiting_approval()
        transporter.enter_box_transporter_inquery_check_discount_per_kilo()
        transporter.enter_box_transporter_inquery_check_currency_unit()
        transporter.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        transporter.enter_box_transporter_inquery_price_unit_option()
        transporter.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        transporter.enter_box_transporter_inquery_per_kilo("4000")
        transporter.enter_box_transporter_inquery_per_kilo_submit()
        transporter.enter_box_transporter_inquery_check_error_currency_unit()
        transporter.enter_box_transporter_inquery_price_unit_select()
        transporter.enter_box_transporter_inquery_price_unit_option2()
        transporter.enter_box_transporter_inquery_per_kilo("4000")
        transporter.enter_box_transporter_inquery_per_kilo_submit()
        transporter.enter_box_transporter_inquery_check_saved_currency_unit()
        b = str(now.strftime("%H:%M"))
        a = transporter.enter_box_transporter_inquery_check_datetime_create()
        assert b in a
        transporter.enter_box_transporter_inquery_click_the_record_is_valid()
        print("زمان ایجاد تخفیف به درستی نمایش داده می شود.")

###box_transporter_inquery_invoice_check_action

    def test04_box_transporter_inquery_invoice_check_action(self):
        transporter = Box_Transporter_Inquery(driver=self.driver)
        sleep(1)
        transporter.enter_box_transporter_inquery_check_table_invoice_click_forwarding_factors()
        transporter.enter_box_transporter_inquery_invoice_action_invoice_valid()
        transporter.enter_box_transporter_inquery_invoice_action_invoice_not_sent()
        transporter.enter_box_transporter_inquery_invoice_action_invoice_no_approval()
        transporter.enter_box_transporter_inquery_check_paid1()

###box_other_service_inquery

    def test05_box_transporter_inquery_check_invoice(self):
        transporter = Box_Transporter_Inquery(driver=self.driver)
        transporter.enter_box_transporter_inquery_check_view_invoice()
        transporter.enter_box_transporter_inquery_click_view_invoice()
        transporter.enter_box_transporter_inquery_invoice_to_person()
        transporter.enter_box_transporter_inquery_invoice_to_person_option()
        transporter.enter_box_transporter_inquery_invoice_to_company_name()
        transporter.enter_box_transporter_inquery_invoice_to_company_name_option()
        transporter.enter_box_transporter_inquery_view_invoice_submit()
        transporter.enter_box_transporter_inquery_view_invoice_error()

###box_transporter_inquery_check_invoice_type

    def test06_box_transporter_inquery_check_invoice_type(self):
        transporter = Box_Transporter_Inquery(driver=self.driver)
        transporter.enter_click_to_box_transporter_inquery()
        sleep(1)
        transporter.enter_box_transporter_inquery_click_invoice_type()
        transporter.enter_box_transporter_inquery_invoice_type_option1()
        transporter.enter_box_transporter_inquery_invoice_type_update()
        sleep(1)
        transporter.enter_box_transporter_inquery_check_table_invoice_click_forwarding_factors()
        sleep(1)
        transporter.enter_box_transporter_inquery_invoice_check_tax_coefficient1()
        transporter.enter_box_transporter_inquery_click_invoice_type()
        transporter.enter_box_transporter_inquery_invoice_type_option2()
        transporter.enter_box_transporter_inquery_invoice_type_update()
        sleep(1)
        transporter.enter_box_transporter_inquery_check_table_invoice_click_forwarding_factors()
        sleep(1)
        transporter.enter_box_transporter_inquery_invoice_check_tax_coefficient2()
        transporter.enter_box_transporter_inquery_invoice_transport_price_unit()
        transporter.enter_box_transporter_inquery_invoice_transport_price_unit_option()
        transporter.enter_box_transporter_inquery_invoice_transport_price_unit_submit()
        transporter.enter_box_transporter_inquery_check_table_invoice_click_forwarding_factors()
        sleep(1)
        transporter.enter_box_transporter_inquery_check_paid3()


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
