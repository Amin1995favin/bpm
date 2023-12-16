from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

from Locators import *
from Pages.Login import LoginPage
from Pages.Orders_Create2 import Orders_Create
from Pages.Find_Element import FindElement
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

###Login

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username("9122367860")
        login.enter_login_btn_submit_next()
        login.enter_login_password("43126")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل شد")

###Orders_Create

    def test02_orders_create(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_new_orders_create()
        findel.wait_until_element_has_an_attribute('xpath', orders_create_name_select, 'class', 'selection')
        orders_create.enter_orders_create_name_select_text("ملیکا کابلی")
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_name_select_option,
                                                   'class', 'select2-results__option select2-results__option--highlighted')
        # orders_create.enter_orders_create_name_select_option()
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("وارد قسمت انتخاب خدمات مورد نیاز شد.")

###orders_create_products

    def test03_orders_create_products(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_orders_create_products_holder()
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        orders_create.enter_orders_create_form_name("دوربین")
        orders_create.enter_orders_create_form_name_en("camera")
        orders_create.enter_orders_create_form_type()
        orders_create.enter_orders_create_form_type_option()
        orders_create.enter_orders_create_form_quantity()
        orders_create.enter_orders_create_form_quantity_option()
        orders_create.enter_orders_create_form_quantity_number("1000")
        orders_create.enter_orders_create_form_one_weight("1")
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_form_length, 'name', '2', 'length')
        # orders_create.enter_orders_create_form_length("30")
        orders_create.enter_orders_create_form_width("50")
        orders_create.enter_orders_create_form_height("20")
        scrolled1= self.driver.find_element('xpath', orders_create_form_quantity_in_box)
        scrolled1.location_once_scrolled_into_view
        # findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_form_quantity_in_box, 'name', '2', 'quantity_in_box')
        orders_create.enter_orders_create_form_quantity_in_box("2")
        # findel.wait_until_element_has_an_attribute('xpath', orders_create_form_price_unit, 'class', '  form-control  validate[maxSize[255]]')
        orders_create.enter_orders_create_form_price_unit()
        orders_create.enter_orders_create_form_price_unit_option()
        orders_create.enter_orders_create_form_one_price("1000")
        # orders_create.enter_orders_create_form_price("2000000")
        orders_create.enter_orders_create_HSCODE()
        orders_create.enter_orders_create_HSCODE_option()
        orders_create.enter_orders_create_form_part_number("112233")
        orders_create.enter_orders_create_form_buy_url("http://testbpm.2ms.ir/")
        scrolled2= self.driver.find_element('xpath', orders_create_form_country)
        scrolled2.location_once_scrolled_into_view
        orders_create.enter_orders_create_form_text("این یک داده تستی می یاشد.")
        orders_create.enter_orders_create_form_country("china")
        orders_create.enter_orders_create_submit_information()
        print("با موفقیت تکمیل اطلاعات سفارش پیش رفتید.")

###Completion_of_information

    def test04_orders_create_ompletion_of_information(self):
        orders_create = Orders_Create(driver=self.driver)
        # scrolled1= self.driver.find_element('xpath', orders_create_information_goback)
        # scrolled1.location_once_scrolled_into_view
        # orders_create.enter_orders_create_information_goback()
        # orders_create.enter_orders_create_chooseservices()
        orders_create.enter_orders_create_information_type()
        orders_create.enter_orders_create_information_type_option()
        orders_create.enter_orders_create_information_transport()
        orders_create.enter_orders_create_information_transport_option()
        scrolled1= self.driver.find_element('xpath', orders_create_information_senders)
        scrolled1.location_once_scrolled_into_view
        # orders_create.enter_orders_create_information_senders("1")
        # orders_create.enter_orders_create_information_must_pay_before_transport()
        # orders_create.enter_orders_create_information_must_pay_before_transport_option()
        sleep(1)
        orders_create.enter_orders_create_information_description("این یک داده تستی می یاشد.")
        orders_create.enter_orders_create_information_pay_in_china()
        orders_create.enter_orders_create_information_pay_in_china_option()
        orders_create.enter_orders_create_information_area_one()
        print("اطلاعات سفارش بررسی شد.")

###information_sender

    def test05_orders_create_information_sender(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        scrolled1= self.driver.find_element('xpath', orders_create_information_sender_name_select)
        scrolled1.location_once_scrolled_into_view
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_sender_city, ' class','select2 select2-container select2-container--default select2-container--below select2-container--focus')
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_information_sender_city_name, 'class', 'Shenzhen', 'select2-search__field')
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_sender_city_option, 'class', 'select2-results__option select2-results__option--highlighted')
        # orders_create.enter_orders_create_information_sender_city()
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_sender_name_select, 'id', 'select2-formsender_p-n1-container')
        # orders_create.enter_orders_create_information_sender_name_select()
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_information_sender_name, 'class', 'ملیکا کابلی', 'select2-search__field')
        # orders_create.enter_orders_create_information_sender_name("ملیکا کابلی")
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_sender_name_option, 'class', 'select2-results__option select2-results__option--highlighted')
        # orders_create.enter_orders_create_information_sender_name_option()
        print("اطلاعات فرستنده بررسی شد.")

###information_receiver

    def test06_orders_create_information_receiver(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        scrolled1= self.driver.find_element('xpath', orders_create_information_receiver_city)
        scrolled1.location_once_scrolled_into_view
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_receiver_city, 'class', 'select2 select2-container select2-container--default')
        # orders_create.enter_orders_create_information_receiver_city()
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_information_receiver_city_name, 'class', 'Tehran', 'select2-search__field')
        # orders_create.enter_orders_create_information_receiver_city_name("Tehran")
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_receiver_city_option, 'class', 'select2-results__option')
        # orders_create.enter_orders_create_information_receiver_city_option()
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_receiver_name_select, 'id', 'select2-formreceiver_p-n1-container')
        # orders_create.enter_orders_create_information_receiver_name_select()
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_information_receiver_name, 'class', 'ملیکا کابلی', 'select2-search__field')
        # orders_create.enter_orders_create_information_receiver_name("ملیکا کابلی")
        sleep(1)
        findel.wait_until_element_has_an_attribute('xpath', orders_create_information_receiver_option, 'class', 'select2-results__option')
        # orders_create.enter_orders_create_information_receiver_option()
        print("اطلاعات گیرنده بررسی شد.")

###factor

    def test07_orders_create_ompletion_of_information_factor(self):
        orders_create = Orders_Create(driver=self.driver)
        scrolled1= self.driver.find_element('xpath', orders_create_information_invoice_to_container)
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_information_sub_bill()
        orders_create.enter_orders_create_information_sub_bill_option()
        orders_create.enter_orders_create_information_factor_rasmi_transport()
        orders_create.enter_orders_create_information_factor_rasmi_transport_option()
        orders_create.enter_orders_create_information_factor_rasmi_clearance()
        orders_create.enter_orders_create_information_need_clearance_inquery()
        orders_create.enter_orders_create_information_need_clearance_inquery_option()
        orders_create.enter_orders_create_information_clearance_youan_invoice_request()
        orders_create.enter_orders_create_information_clearance_youan_invoice_request_option()
        orders_create.enter_orders_create_information_factor_rasmi()
        orders_create.enter_orders_create_information_factor_rasmi_option()
        orders_create.enter_orders_create_information_invoice_to_container()
        orders_create.enter_orders_create_information_invoice_to_container_name("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_information_invoice_to_container_option()
        orders_create.enter_orders_create_information_approve()
        print("اطلاعات فاکتور و پیش فاکتور بررسی شد.")
        orders_create.enter_orders_create_next_review()
        print("بررسی نهایی سفارش انجام شد.")
        orders_create.enter_click_checking_the_order()
        orders_create.enter_check_the_order_approved()
        print("جزییات سفارش تایید شد.")

###clearance_inquiry

    def test08_orders_create_clearance_inquiry(self):
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_clearance_inquiry()
        orders_create.enter_clearance_inquiry_cargo_clearance()
        findel.wait_until_element_has_an_attribute('xpath', clearance_inquiry_cargo_clearance_option, 'data-select2-id', '28')
        # orders_create.enter_clearance_inquiry_cargo_clearance_option()
        orders_create.enter_clearance_inquiry_type()
        orders_create.enter_clearance_inquiry_type_option()
        orders_create.enter_clearance_inquiry_Price("50,000,000")
        orders_create.enter_clearance_inquiry_Price_unit()
        orders_create.enter_clearance_inquiry_comment("این یک کامنت تست می باشد.")
        orders_create.enter_clearance_inquiry_form_save()
        print("یک استعلام فاکتور ترخیص با موفقیت صادر شد.")

###other_inquiries

    def test09_orders_create_other_inquiries(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_click_other_inquiries()
        orders_create.enter_other_inquiries_services_invoice_type()
        orders_create.enter_other_inquiries_services_invoice_type_option()
        orders_create.enter_other_inquiries_services_invoice_type_update()
        orders_create.enter_other_inquiries_pre_factor_type()
        orders_create.enter_other_inquiries_price("2000000")
        orders_create.enter_other_inquiries_price_unit()
        orders_create.enter_other_inquiries_price_unit_option()
        orders_create.enter_other_inquiries_description("این یک تست برای سایر استعلام ها است.")
        orders_create.enter_other_inquiries_save_submit()
        print("بخش سایر استعلام ها بررسی شد.")








    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
