from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert

from Locators import *
from Pages.Box_Chat import Box_Chat
from Pages.Box_Order_Details import Box_Order_Details
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
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
        login.enter_login_username("9020981024")
        login.enter_login_btn_submit_next()
        login.enter_login_password("34567")
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")

###Orders_Create

    def test02_orders_create(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_click_orders()
        orders_create.enter_click_orders_create()
        orders_create.enter_orders_create_name_select()
        orders_create.enter_orders_create_name_select_text("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_name_select_option()
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        print("وارد قسمت انتخاب خدمات مورد نیاز شد.")

###orders_check_create_no_products

    def test03_orders_check_create_no_products(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()
        orders_create.enter_orders_create_information_approve()
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_product_details_of_this_order_are_approved()
        sleep(2)
        orders_create.enter_product_error_details_of_this_order_are_approved()

    ###create_order_product_check_form

    def test04_create_order_product_check_form(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_product_click_edit_order()
        orders_create.enter_orders_create_chooseservices()
        sleep(1)
        orders_create.enter_click_create_order_product()
        orders_create.enter_create_order_product_check_form()
        orders_create.enter_create_order_product_check_selection()

###orders_create_products_not_data

    def test05_orders_create_products_not_data(self):
        orders_create = Orders_Create(driver=self.driver)
        # orders_create.enter_click_create_order_product()
        scrolled1= self.driver.find_element('xpath', orders_create_submit_information)
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        print("هیج دیتایی وارد نشده است.")

###orders_create_products_not_data

    def test06_orders_create_products_not_data(self):
        orders_create = Orders_Create(driver=self.driver)
        scrolled2= self.driver.find_element('xpath', orders_create_category_select)
        scrolled2.location_once_scrolled_into_view
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        scrolled1= self.driver.find_element('xpath', orders_create_submit_information)
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

    def test07_orders_create_products(self):
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

    def test08_orders_create_products_check_price_unit(self):
        orders_create = Orders_Create(driver=self.driver)
        alert = Alert(driver=self.driver)
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
        orders_create.enter_orders_create_form_price_unit_option2()
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
        alert.accept()
        self.driver.refresh()
        print(" واحد قیمت کالای شما دلار است درصورتی که قبلا کالایی با واحد قیمت ریال تعریف کرده اید. کالاهای یک سفارش نمی تواند واحدهای متفاوتی داشته باشد.")

###orders_create_products_check_price_unit

    def test09_orders_create_products_check_price_unit(self):
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

###check_box_order_details

    def test10_check_box_order_details_form(self):
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_form_details()
        order_details.enter_check_box_order_details_form_order_goods()
        order_details.enter_check_box_order_details_form_customer_declared_goods()
        order_details.enter_check_box_order_details_form_all_order_files()
        order_details.enter_check_box_order_details_form_order_notes()
        order_details.enter_check_box_order_details_form_logs()

###check_box_order_details

    def test11_check_box_order_details(self):
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_order_types()
        order_details.enter_check_box_order_type_of_shipping()
        order_details.enter_check_box_order_details_other_services_invoice_type()
        order_details.enter_check_box_order_details_total_volumetric_weight()
        order_details.enter_check_box_order_details_unit_of_value()
        order_details.enter_check_box_order_details_required_services()
        order_details.enter_check_box_order_details_clearance_invoice_type()
        order_details.enter_check_box_order_details_total_actual_weight()
        order_details.enter_check_box_order_details_total_chargeable_weight()
        order_details.enter_check_box_order_details_total_value()
        order_details.enter_check_box_order_details_order_owner()
        order_details.enter_check_box_order_details_receivers_city()
        order_details.enter_check_box_order_details_senders_city()
        order_details.enter_check_box_order_details_customer_manager()
        order_details.enter_check_box_order_details_marketer()
        order_details.enter_check_box_order_details_creator()
        order_details.enter_check_box_order_details_branch_representation()

###check_box_order_details_order_goods

    def test12_check_box_order_details_order_goods(self):
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_order_goods1()
        order_details.enter_check_box_order_details_order_goods2()

###check_create_box_chat

    def test13_check_create_box_chat(self):
        box_chat = Box_Chat(driver=self.driver)
        box_chat.enter_click_box_chat()
        sleep(1)
        box_chat.enter_box_chat_text("سلام")
        box_chat.enter_box_chat_contact("ملیکا کابلی")
        sleep(1)
        box_chat.enter_box_chat_contact_option()
        box_chat.enter_box_chat_submit()
        box_chat.enter_box_chat_check_text()
        box_chat.enter_box_chat_check_customer_manager()
        box_chat.enter_box_chat_check_contact()
        box_chat.enter_box_chat_check_contact_location()
        box_chat.enter_box_chat_check_edite()
        print("سابقه مذاکرات چک و صحیح می باشد.")

###orders_create_products_check_price_unit

    def test14_check_box_clearance_inquery(self):
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_click_box_clearance_inquiry()
        sleep(2)
        orders_create.enter_check_box_clearance_inquery_check()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
