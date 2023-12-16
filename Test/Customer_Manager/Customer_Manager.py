from persian import persian
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from persiantools.jdatetime import JalaliDate
from datetime import datetime
from translate import translator
import convert_numbers
from unidecode import unidecode


from Pages.Customer_Manager.Box_Other_Service_Inquery import Box_Other_Service_Inquery
from Pages.Login import LoginPage
from Pages.Customer_Manager.Box_Transporter_Inquery import Box_Transporter_Inquery
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

###Login_customer_manager

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
        customer_manager = Box_Transporter_Inquery(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id()
        customer_manager.enter_click_box_transporter_inquery()
        sleep(2)
        customer_manager.enter_box_transporter_inquery_check_table_results()
        customer_manager.enter_box_transporter_inquery_check_table_invoice_forwarding_factors()
        customer_manager.enter_box_transporter_inquery_check_table_list_of_shipping_discounts_per_kilo()
        customer_manager.enter_box_transporter_inquery_check_table_estimated_transportation_cost()
        customer_manager.enter_box_transporter_inquery_check_table_request_a_discount_on_shipping_per_kilo()
        customer_manager.enter_box_transporter_inquery_check_table_currency_of_invoice_shipping()
        customer_manager.enter_box_transporter_inquery_check_table_transportation_invoice_type()

###box_transporter_inquery_check_datetime

    def test03_box_transporter_inquery_check_datetime(self):
        customer_manager = Box_Transporter_Inquery(driver=self.driver)
        customer_manager.enter_box_transporter_inquery_price_unit_select()
        customer_manager.enter_box_transporter_inquery_price_unit_option()
        customer_manager.enter_box_transporter_inquery_price_unit_select()
        customer_manager.enter_box_transporter_inquery_click_the_record_is_valid()
        customer_manager.enter_box_transporter_inquery_per_kilo("-50000")
        customer_manager.enter_box_transporter_inquery_per_kilo_submit()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_check_error_discount_per_kil()
        customer_manager.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_price_unit_option()
        # customer_manager.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_per_kilo("50000")
        customer_manager.enter_box_transporter_inquery_per_kilo_submit()
        now = datetime.now()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_check_is_it_valid()
        customer_manager.enter_box_transporter_inquery_check_the_record_is_valid()
        customer_manager.enter_box_transporter_inquery_check_awaiting_approval()
        customer_manager.enter_box_transporter_inquery_check_discount_per_kilo()
        customer_manager.enter_box_transporter_inquery_check_currency_unit()
        customer_manager.enter_box_transporter_inquery_price_unit_select()
        customer_manager.enter_box_transporter_inquery_price_unit_option()
        # customer_manager.enter_box_transporter_inquery_price_unit_select()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_per_kilo("4000")
        customer_manager.enter_box_transporter_inquery_per_kilo_submit()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_check_error_currency_unit()
        customer_manager.enter_box_transporter_inquery_price_unit_select()
        customer_manager.enter_box_transporter_inquery_price_unit_option2()
        customer_manager.enter_box_transporter_inquery_per_kilo("4000")
        customer_manager.enter_box_transporter_inquery_per_kilo_submit()
        sleep(1)
        customer_manager.enter_box_transporter_inquery_check_saved_currency_unit()

        b = print(now.strftime("%H:%M"))
        sleep(1)
        a = customer_manager.enter_box_transporter_inquery_check_datetime_create()
        a = persian.convert_fa_numbers(a)
        b = str(b)
        assert b in a
        print("زمان به درستی نمایش داده می شود.")

###box_other_service_inquery

    def test04_create_box_other_service_inquery(self):
        box_other = Box_Other_Service_Inquery(driver=self.driver)
        box_other.enter_click_box_other_service_inquery()
        sleep(1)
        box_other.enter_box_other_service_inquery_check_record()
        box_other.enter_box_other_service_inquery_check_other_services_invoice_type()
        box_other.enter_box_other_service_inquery_check_other_inquiries()
        box_other.enter_box_other_service_inquery_other_inquery_type()
        box_other.enter_box_other_service_inquery_other_inquery_type_option()
        box_other.enter_box_other_service_inquery_price("600")
        box_other.enter_box_other_service_inquery_price_unit()
        box_other.enter_box_other_service_inquery_price_unit_option()
        sleep(1)
        box_other.enter_box_other_service_inquery_submit()
        print("یک پیش فاکتور سایر استعلام ها ایجاد شد.")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
