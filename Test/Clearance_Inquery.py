from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from Locators import *
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Clearance_Inquery import Clearance_Inquery
import unittest
# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

###Login

    def test01_login(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9109901340")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد")

###Orders_view

    def test02_Orders_view(self):
        orders_create = Orders_Create(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id()
        clearance_inquery.enter_click_box_clearance_inquery()
        print("وارد قسمت استعلام ترخیص شد.")

###clearance_inquery_check_no_data

    def test03_clearance_inquery_check_no_data(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_click_box_clearance_inquery_submit()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        print(" وارد کردن قیمت الزامی می باشد!")

###check_box_clearance_inquery

    def test04_check_box_clearance_inquery(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_clearance_inquery_price("500")
        sleep(1)
        clearance_inquery.enter_box_clearance_inquery_the_weight_of_each_clove()
        clearance_inquery.enter_box_clearance_inquery_cheng_factor_rasmi_option2()
        clearance_inquery.enter_box_clearance_inquery_cheng_factor_rasmi_option1()

###check_declared_price

    def test05_conversion_rate_to_iranian_rial(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_clearance_inquery_price("500")
        sleep(2)
        clearance_inquery.enter_check_declared_price()

###box_clearance_check_form

    def test06_box_clearance_check_form(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_clearance_check_form_tax_return()
        clearance_inquery.enter_box_clearance_check_form_inquiry()
        clearance_inquery.enter_box_clearance_check_form_invoices()
        clearance_inquery.enter_box_clearance_check_form_proof_of_dead()
        clearance_inquery.enter_box_clearance_check_form_pre_evaluation_notes()
        clearance_inquery.enter_box_clearance_check_form_clearance_inquiry_code()
        clearance_inquery.enter_box_clearance_check_form_customs_purchase_link()
        clearance_inquery.enter_box_clearance_check_form_clearance_invoice_type()
        clearance_inquery.enter_box_clearance_check_form_billing_delivery_information()
        clearance_inquery.enter_box_clearance_check_form_user_notes()
        clearance_inquery.enter_box_clearance_check_form_issue_clearance_inquiry()

###box_clearance_check_form

    def test07_box_clearance_check_len_form(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        a= clearance_inquery.enter_box_clearance_check_len_invoices()
        b= clearance_inquery.enter_box_clearance_check_len_inquiry()
        clearance_inquery.enter_box_clearance_inquery_price("500")
        clearance_inquery.enter_box_clearance_click_full_invoice()
        clearance_inquery.enter_click_box_clearance_inquery_submit()
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        sleep(2)
        c= clearance_inquery.enter_box_clearance_check_inquiry_box()
        c= clearance_inquery.enter_box_clearance_check_len_invoices()
        d= clearance_inquery.enter_box_clearance_check_len_inquiry()
        print(a)
        print(c)
        print(b+1)
        print(d)
        assert a == c
        assert b+1 == d
        print("یک استعلام به استعلام های قبلی اضافه شد.")
        print("هیج پیش فاکتوری به پیش فاکتورهای قبلی اضافه نشد.")
        clearance_inquery.enter_box_clearance_inquery_price("500")
        clearance_inquery.enter_click_box_clearance_inquery_submit()
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_box_clearance_click_checking_shipping_cost()
        sleep(2)
        e= clearance_inquery.enter_box_clearance_check_len_invoices()
        g = clearance_inquery.enter_box_clearance_check_len_inquiry()
        print(c+1)
        print(e)
        print(d+1)
        print(g)
        assert c+1 == e
        assert d+1 == g
        print("هیج استعلامی به پیش استعلام های قبلی اضافه نشد.")
        print("یک پیش فاکتور به پیش فاکتورهای قبلی اضافه شد.")

###check_final_price

    def test08_check_final_price(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_clearance_inquery_price("500")
        clearance_inquery.enter_clearance_inquiry_Price_unit()
        clearance_inquery.enter_clearance_inquiry_Price_unit_option4()
        sleep(2)
        clearance_inquery.enter_check_final_price()

###check_invoice

    def test09_check_invoice(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_clearance_inquery_price("500")
        clearance_inquery.enter_click_box_clearance_inquery_submit()
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_box_clearance_invoice_check_Price()
        clearance_inquery.enter_box_clearance_invoice_check_interest_rate()
        clearance_inquery.enter_box_clearance_invoice_check_total_actual_weight()
        clearance_inquery.enter_box_clearance_invoice_check_final_price()
        clearance_inquery.enter_box_clearance_invoice_check_tax_coefficient()
        clearance_inquery.enter_box_clearance_invoice_check_payments_list()
        clearance_inquery.enter_box_clearance_invoice_check_awaiting_Payment()

###conversion_rate_to_iranian_rial

    def test10_conversion_rate_to_iranian_rial(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_order_details_check_color_checking_Shipping_Cost()
        clearance_inquery.enter_check_conversion_rate_to_iranian_rial1()


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
