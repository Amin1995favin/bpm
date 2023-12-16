from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert

from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Box_Invoices import Box_Invoices
from Pages.Customer_Manager.Box_Other_Service_Inquery import Box_Other_Service_Inquery

from Locators import *
from Pages.Box_Chat import Box_Chat
from Pages.Box_Order_Details import Box_Order_Details
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Find_Element import FindElement
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
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9020981024")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

###Orders_Create

    def test02_orders_create(self):
        orders_create = Orders_Create(driver=self.driver)
        sleep(1)
        orders_create.enter_click_feather_light_content()
        orders_create.enter_click_orders()
        sleep(2)
        orders_create.enter_click_feather_light_content2()
        orders_create.enter_click_orders_create()
        orders_create.enter_orders_create_name_select()
        orders_create.enter_orders_create_name_select_text("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_name_select_option()
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("وارد قسمت انتخاب خدمات مورد نیاز شد.")

###orders_create_products_not_data

    def test03_orders_create_products_not_data(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_click_create_order_product()
        # self.driver.execute_script("window.scrollBy(-400, 400)")
        scrolled2 = self.driver.find_element('xpath', orders_create_category_select)
        scrolled2.location_once_scrolled_into_view
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        scrolled1 = self.driver.find_element('xpath', orders_create_submit_information)
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        print("با انتخاب فقط دسته بندی کلی کالا نمی توان به مرحله بعد رفت.")
        orders_create.enter_orders_create_form_name_en("دوربین")
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        print("نام انگلیسی کالا بصورت انگلیسی وارد نشده است.")
        orders_create.enter_orders_create_form_name_en("camera")
        orders_create.enter_orders_create_form_type()
        orders_create.enter_orders_create_form_type_option()
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        print("باید تعداد وارد شود.")
        orders_create.enter_orders_create_form_quantity_number("1000")
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        print("باید وزن واحد وارد شود.")
        orders_create.enter_orders_create_form_one_weight("1")
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        sleep(3)
        print("با موفقیت تکمیل اطلاعات سفارش انجام شد.")
        orders_create.enter_create_order_product_check_passed()

###orders_create_new_products

    def test04_orders_create_products(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_create_order_product()
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        orders_create.enter_orders_create_form_name("دوربین2")
        orders_create.enter_orders_create_form_name_en("camera2")
        orders_create.enter_orders_create_form_type()
        orders_create.enter_orders_create_form_type_option()
        orders_create.enter_orders_create_form_quantity()
        orders_create.enter_orders_create_form_quantity_option()
        orders_create.enter_orders_create_form_quantity_number("20")
        orders_create.enter_orders_create_form_one_weight("2")
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_form_length, 'name', '2',
                                                            'length')
        orders_create.enter_orders_create_form_width("50")
        orders_create.enter_orders_create_form_height("20")
        scrolled1 = self.driver.find_element('xpath', orders_create_form_quantity_in_box)
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_form_quantity_in_box("2")
        orders_create.enter_orders_create_form_price_unit()
        orders_create.enter_orders_create_form_price_unit_option()
        orders_create.enter_orders_create_form_one_price("20")
        orders_create.enter_orders_create_HSCODE()
        orders_create.enter_orders_create_HSCODE_option()
        orders_create.enter_orders_create_form_part_number("112233")
        orders_create.enter_orders_create_form_buy_url("http://testbpm.2ms.ir/")
        scrolled2 = self.driver.find_element('xpath', orders_create_form_country)
        scrolled2.location_once_scrolled_into_view
        orders_create.enter_orders_create_form_text("این دومین داده تستی می یاشد.")
        orders_create.enter_orders_create_form_country("china")
        orders_create.enter_orders_create_submit_information()
        sleep(3)
        print("با موفقیت کالا اضافه شد.")
        orders_create.enter_create_order_product_check_passed2()

###orders_create_products_check_price_unit

    def test05_orders_create_products_check_price_unit(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()
        orders_create.enter_orders_create_information_approve()
        orders_create.enter_create_order_product_check_all_data()
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_check_color_checking_the_order()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_product_details_of_this_order_are_approved()
        sleep(1)
        orders_create.enter_box_order_details_check_color_btn()
        orders_create.enter_box_order_details_check_log()
        orders_create.enter_product_check_edit_order()

###check_box_order_details_order_goods

    def test06_check_box_order_details_order_goods(self):
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_order_goods1()
        order_details.enter_check_box_order_details_order_goods2()

###box_other_service_inquery

    def test07_create_box_other_service_inquery(self):
        box_other = Box_Other_Service_Inquery(driver=self.driver)
        box_other.enter_click_box_other_service_inquery()
        box_other.enter_box_other_service_inquery_other_inquery_type()
        box_other.enter_box_other_service_inquery_other_inquery_type_option()
        box_other.enter_box_other_service_inquery_price("600")
        box_other.enter_box_other_service_inquery_price_unit()
        box_other.enter_box_other_service_inquery_price_unit_option()
        sleep(1)
        box_other.enter_box_other_service_inquery_submit()
        print("یک پیش فاکتور سایر استعلام ها ایجاد شد.")

###Login_clearance_inquery

    def test08_login_clearance(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9109901340")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد")

###Orders_view

    def test09_Orders_view(self):
        orders_create = Orders_Create(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id()
        clearance_inquery.enter_click_box_clearance_inquery()
        print("وارد قسمت استعلام ترخیص شد.")

###create_box_clearance

    def test10_create_box_clearance(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        clearance_inquery.enter_box_clearance_check_len_invoices()
        clearance_inquery.enter_box_clearance_check_len_inquiry()
        clearance_inquery.enter_box_clearance_inquery_price("500")
        # clearance_inquery.enter_box_clearance_click_full_invoice()
        clearance_inquery.enter_click_box_clearance_inquery_submit()
        clearance_inquery.enter_click_alert()
        clearance_inquery.enter_click_alert()

###Login_customer_manager

    def test11_login_customer_manager(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9020981024")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

###box_invoices_check

    def test12_box_invoices_check(self):
        orders_create = Orders_Create(driver=self.driver)
        box_invoices = Box_Invoices(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id()
        orders_create.enter_click_checking_the_order()
        box_invoices.enter_click_box_invoices()
        box_invoices.enter_box_invoices_check_invoice_list()
        box_invoices.enter_box_invoices_check_approvals_final_settlement_order()
        box_invoices.enter_box_invoices_check_approvals_financial_for_international_transportation()
        box_invoices.enter_box_invoices_check_pick_up_order()
        box_invoices.enter_box_invoices_check_change_pro_invoice_owner()
        box_invoices.enter_box_invoices_check_send_aggregate_link()
        box_invoices.enter_box_invoices_check_filter_clearance()
        box_invoices.enter_box_invoices_check_filter_other_services()
        box_invoices.enter_box_invoices_check_filter_shipping_cost()

###box_invoices_sent_customer

    def test13_box_invoices_sent_customer(self):
        box_invoices = Box_Invoices(driver=self.driver)
        box_invoices.enter_box_invoices_click_filter_other_services()
        box_invoices.enter_box_invoices_click_filter_clearance()
        driver.set_window_size(480, 640)
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[3]/td[9]/a")
        # scrolled1 = self.driver.find_element('xpath', "//tbody/tr[1]/td[8]")
        # scrolled1 = self.driver.find_element('xpath', "#boxinvoices179618 > td:nth-child(9) > div:nth-child(2) > a.btn.btn-sm.btn-info.btn-block.n-border-left")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        # driver.execute_script("document.querySelector('table td:last-child').scrollIntoView()")
        # self.driver.execute_script("window.scrollBy(300, 0)")
        # driver.set_window_size(480, 640)
        # element = driver.find_element('xpath', '//tbody/tr[1]/td[7]')
        # sleep(1)
        # element.location_once_scrolled_into_view
        # sleep(3)
        sleep(1)
        box_invoices.enter_box_invoices_not_sent_to_the_customer()
        box_invoices.enter_box_invoices_click_filter_other_services()
        box_invoices.enter_box_invoices_click_filter_clearance()
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[3]/td[9]/a")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        box_invoices.enter_box_invoices_no_customer_approval()
        box_invoices.enter_box_invoices_click_filter_other_services()
        box_invoices.enter_box_invoices_click_filter_clearance()
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[3]/td[9]/a")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
        box_invoices.enter_box_invoices_click_send_to_whatsapp()

###box_pickup_check

    def test14_box_pickup_check(self):
        self.driver.maximize_window()
        box_pickup = Box_Pickup(driver=self.driver)
        box_pickup.enter_click_cargo_pickup()
        box_pickup.enter_box_pickup_check_order()
        box_pickup.enter_box_pickup_check_internal_carriage()
        box_pickup.enter_box_pickup_sender_information()

###box_pickup_send_pickup_command

    def test15_box_pickup_send_pickup_command(self):
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
