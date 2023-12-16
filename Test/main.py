from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.alert import Alert
import os

from Locators import *
from Pages.Box_Chat import Box_Chat
from Pages.Box_Order_Details import Box_Order_Details
from Pages.Clearance.My_Tasks import My_Tasks
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Box_Invoices import Box_Invoices
from Pages.Customer_Manager.Box_Other_Service_Inquery import Box_Other_Service_Inquery
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Box_Transporter_Inquery import Box_Transporter_Inquery
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Financial_Manager.financial_manager import Financial_Manager
from Pages.Login import LoginPage
from datetime import datetime
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Find_Element import FindElement
import unittest

from Pages.MongoDB.Mongo import Mongodb
from Pages.Persons import Persons
from Pages.Warehouses.Warehouses import Warehouses
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_main(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        # cls.driver.minimize_window()
        cls.tests_texts = []


    ################### Login_customer_manager ###################

    def test01_login_customer_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        message = "با موفقیت وارد پنل مدیر مشتری شد"
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    ################### Orders_Create ###################

    def test02_orders_create(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        sleep(1)
        # orders_create.enter_click_feather_light_content()
        orders_create.enter_click_orders()
        sleep(2)
        # orders_create.enter_click_feather_light_content2()
        orders_create.enter_click_orders_create()
        orders_create.enter_orders_create_name_check()
        orders_create.enter_orders_create_name_select()
        orders_create.enter_orders_create_name_select_text("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_name_select_option()
        orders_create.enter_orders_create_check_transport()
        orders_create.enter_orders_create_check_clearance()
        orders_create.enter_orders_create_chooseservices()
        message = "با موفقیت وارد قسمت انتخاب خدمات مورد نیاز شد."
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    ################### orders_check_create_no_products ###################

    def test03_orders_check_create_no_products(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_choose_services_check()
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()
        orders_create.enter_orders_create_information_approve()
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_product_details_of_this_order_are_approved()
        sleep(2)
        orders_create.enter_product_error_details_of_this_order_are_approved()
        self.tests_texts.append("تایید سفارش بدون کالا به درستی بررسی شد. ")
        print("############################################")

    ################### create_order_product_check_form ###################

    def test04_create_order_product_check_form(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_product_click_edit_order()
        orders_create.enter_orders_create_chooseservices()
        sleep(1)
        orders_create.enter_click_create_order_product()
        orders_create.enter_create_order_product_check_form()
        orders_create.enter_create_order_product_check_selection()
        self.tests_texts.append("تعداد المان های در فرم کالا بررسی شد.")
        print("############################################")

    ################### orders_create_products_not_data ###################

    def test05_orders_create_products_not_data(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        # orders_create.enter_click_create_order_product()
        scrolled1 = self.driver.find_element('xpath', orders_create_submit_information)
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        print("هیج دیتایی وارد نشده است.")
        self.tests_texts.append("بررسی ایجاد فرم بدون دیتا انجام شد. ")
        print("############################################")

    ################### orders_create_products ###################

    def test06_orders_create_products(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        scrolled2 = self.driver.find_element('xpath', orders_create_category_select)
        scrolled2.location_once_scrolled_into_view
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        orders_create.enter_orders_create_detailed_classification_of_goods()
        sleep(1)
        orders_create.enter_orders_create_detailed_classification_of_goods_option()
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
        sleep(1)
        print("با موفقیت تکمیل اطلاعات سفارش انجام شد.")
        # orders_create.enter_create_order_product_check_passed()
        # driver.implicitly_wait(10)
        # print(datetime.now())
        # try:
        sleep(2)
        orders_create.enter_create_order_product_check_passed()
        # ________________________________________________________________
        # except:
        sleep(1)
        # print(datetime.now())
        self.tests_texts.append("فرم ایجاد و دیتای مشاهده شده درست می باشد.")
        print("############################################")

    ################### orders_create_new_products ###################

    def test07_orders_create_products(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_create_order_product()
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        orders_create.enter_orders_create_detailed_classification_of_goods()
        sleep(.3)
        orders_create.enter_orders_create_detailed_classification_of_goods_option()
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
        message = "با موفقیت کالا اضافه شد."
        print(message)
        self.tests_texts.append(message)
        orders_create.enter_create_order_product_check_passed2()
        print("############################################")

    ################### orders_create_products_check_price_unit ###################

    def test08_orders_create_products_check_price_unit(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        alert = Alert(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_create_order_product()
        orders_create.enter_orders_create_category_select()
        sleep(.3)
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
        print(
            " واحد قیمت کالای شما دلار است درصورتی که قبلا کالایی با واحد قیمت ریال تعریف کرده اید. کالاهای یک سفارش نمی تواند واحدهای متفاوتی داشته باشد.")
        self.tests_texts.append("بررسی ایجاد نشدن کالا با یک واحد قیمیتی متفاوت انجام شد.")
        print("############################################")

    ################### orders_create_products_check_price_unit ###################

    def test09_orders_create_products_check_price_unit(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_sender_city_btn()
        orders_create.enter_orders_create_check_receiver_city_btn()
        orders_create.enter_orders_create_information_approve()
        orders_create.enter_create_order_product_check_all_data()
        # ________________________________________________________________
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_check_color_checking_the_order()
        orders_create.enter_product_click_checking_the_order()
        # orders_create.enter_product_details_of_this_order_are_approved()
        sleep(1)
        # orders_create.enter_box_order_details_check_color_btn()
        # scrolled1 = self.driver.find_element('xpath', "//*[@id='orderstatus']/div/div[2]/table/tbody/tr/td[2]")
        # sleep(1)
        # scrolled1.location_once_scrolled_into_view
        # orders_create.enter_box_order_details_check_log()
        orders_create.enter_product_check_edit_order()
        self.tests_texts.append("شهر ارسال و دریافت انتخاب و به مرحله بعد فرستاده شد. ")
        print("############################################")

    ################### check_box_order_details ###################

    def test10_check_box_order_details_form(self):
        self.driver.implicitly_wait(10)
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_form_details()
        # ________________________________________________________________
        order_details.enter_check_box_order_details_form_order_goods()
        order_details.enter_check_box_order_details_form_customer_declared_goods()
        order_details.enter_check_box_order_details_form_all_order_files()
        order_details.enter_check_box_order_details_form_order_notes()
        order_details.enter_check_box_order_details_form_logs()
        self.tests_texts.append("جزئیات سفارش بررسی شد. ")
        print("############################################")

    ################### check_box_order_details ###################

    def test11_check_box_order_details(self):
        self.driver.implicitly_wait(10)
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_order_types()
        order_details.enter_check_box_order_type_of_shipping()
        order_details.enter_check_box_order_details_other_services_invoice_type()
        order_details.enter_check_box_order_details_total_volumetric_weight()
        # ________________________________________________________________
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
        # order_details.enter_check_box_order_details_marketer()
        order_details.enter_check_box_order_details_creator()
        order_details.enter_check_box_order_details_branch_representation()
        self.tests_texts.append("همه جزئیات سفارش بررسی شد. ")
        print("############################################")

    ################### check_box_order_details_order_goods ###################

    def test12_check_box_order_details_order_goods(self):
        self.driver.implicitly_wait(10)
        order_details = Box_Order_Details(driver=self.driver)
        order_details.enter_check_box_order_details_order_goods1()
        order_details.enter_check_box_order_details_order_goods2()
        self.tests_texts.append("تمام بخش های کالای اول و دوم بررسی شد. ")
        print("############################################")

    ################### check_create_box_chat ###################

    def test13_check_create_box_chat(self):
        self.driver.implicitly_wait(10)
        box_chat = Box_Chat(driver=self.driver)
        box_chat.enter_click_box_chat()
        sleep(1)
        box_chat.enter_box_chat_check()
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
        message = "سابقه مذاکرات چک و صحیح می باشد."
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    ################### review_and_correct_order ###################

    def test14_review_and_correct_order(self):
        self.driver.implicitly_wait(15)
        tasks_list = Tasks_list(driver=self.driver)
        sleep(1)
        order_id = tasks_list.enter_return_order_id()
        print(order_id)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_review_and_correct_order()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter(order_id)
        # tasks_list.enter_customer_manager_date_filter(order_id)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_correct_order()
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_correct_order_btn)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_correct_order_btn()
        message = "جزئیات سفارش مورد نظر تایید شد. "
        print(message)
        self.tests_texts.append(message)
        sleep(1)
        # tasks_list.enter_customer_manager_update_my_tasks()
        # sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_assert_correct_order()
        print("############################################")

        ################### Login_clearance_inquery ###################

        # def test16_login_clearance(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_clearance)
        sleep(1)
        login.enter_login_btn_submit_next()
        sleep(1)
        login.enter_login_password(code_no_admin)
        sleep(1)
        login.enter_login_btn_submit()
        sleep(1)
        message = "با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد"
        print(message)
        self.tests_texts.append(message)
        print("############################################")

        ################### clearance_my_tasks_need_to_issue ###################

        # def test17_clearance_my_tasks_need_to_issue(self):
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        # self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[2]/div[1]/div[1]/ul/li[4]/a").click()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_need_clearance_inquiry()
        my_tasks.enter_clearance_my_tasks_update()
        sleep(1)
        self.driver.refresh()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_search(order_id)
        sleep(1)
        my_tasks.enter_clearance_my_tasks_search_btn()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_need_to_issue()
        my_tasks.enter_clearance_my_tasks_need_to_issue2()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_need_to_issue()
        sleep(3)
        my_tasks.enter_clearance_my_tasks_need_to_issue_check()
        scrolled2 = self.driver.find_element('xpath', clearance_my_tasks_need_to_issue_price)
        scrolled2.location_once_scrolled_into_view
        my_tasks.enter_clearance_my_tasks_need_to_issue_price(2000000)
        my_tasks.enter_clearance_my_tasks_need_to_issue_price_unit()
        sleep(0.3)
        my_tasks.enter_clearance_my_tasks_need_to_issue_price_unit_option()
        scrolled3 = self.driver.find_element('xpath', clearance_my_tasks_need_to_issue_btn)
        sleep(1)
        scrolled3.location_once_scrolled_into_view
        sleep(2)
        my_tasks.enter_clearance_my_tasks_need_to_issue_btn()
        sleep(2)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(2)
        message = "پیش فاکتور صادر شد. "
        print(message)
        self.tests_texts.append(message)
        # sleep(5)
        # my_tasks.enter_clearance_my_tasks_update()
        # sleep(1)
        # my_tasks.enter_clearance_my_tasks_search(order_id)
        # my_tasks.enter_clearance_my_tasks_search_btn()
        # sleep(1)
        # my_tasks.enter_clearance_manager_my_tasks_assert_need_to_issue()
        print("############################################")

    ################### Login_customer_manager ###################

    def test15_login_customer_manager(self):
        self.driver.implicitly_wait(5)
        a = self.driver.find_element('xpath', clearance_my_tasks_search)
        b = a.get_attribute('value')
        print(b)
        self.driver.get(base_url)
        tasks_list = Tasks_list(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        message = "با موفقیت وارد پنل مدیر مشتری شد"
        print(message)
        self.tests_texts.append(message)
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_date_filter(b)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        print("############################################")

    def test16_review_and_correct_order(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', clearance_my_tasks_search)
        b = a.get_attribute('value')
        print(b)
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_to_customer()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(b)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(0.3)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        # sleep(1)
        # driver.set_window_size(480, 640)
        sleep(1)
        all_handle = self.driver.window_handles
        sleep(1)
        self.driver.switch_to.window(all_handle[1])
        sleep(1)
        sleep(1)
        scrolled1 = self.driver.find_element('xpath',
                                             "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[9]/div[2]/a[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance_check()
        tasks_list.enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer()
        print("فاکتور حمل به مشتری ارسال شد. ")
        sleep(1)
        # scrolled2 = self.driver.find_element('xpath',
        #                                      "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[9]/div[2]/a[1]")
        # sleep(1)
        # scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance_not_sent_to_the_customer()
        print("فاکتور ترخیص به مشتری ارسال شد. ")
        tasks_list.enter_customer_manager_my_tasks()
        # self.driver.refresh()
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(b)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        sleep(1)
        all_handle1 = self.driver.window_handles
        sleep(1)
        self.driver.switch_to.window(all_handle1[2])
        sleep(1)
        scrolled3 = self.driver.find_element('xpath',
                                             "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[9]/div[3]/a[1]")
        sleep(1)
        scrolled3.location_once_scrolled_into_view
        sleep(.4)
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_approval()
        print("فاکتور حمل توسط مشتری تایید شد. ")
        sleep(1)
        # scrolled4 = self.driver.find_element('xpath',
        #                                      "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[9]/div[2]/a[1]")
        # sleep(1)
        # scrolled4.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_no_customer_approval()
        print("فاکتور ترخیص توسط مشتری تایید شد. ")
        self.tests_texts.append("فاکتور حمل و ترخیص برای مشتری ارسال و تایید شدند. ")

        print("############################################")

    ################### auto_need_pick_up_order ###################

    def test17_auto_need_pick_up_order(self):
        self.driver.implicitly_wait(10)
        # orders_create = Orders_Create(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        a = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[1]/h1/a[1]/span").text
        b = print(a)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_auto_need_pick_up_order()
        tasks_list.enter_customer_manager_update_my_tasks()
        # scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[2]/div/div/div/div/div/div/div/form/div/input")
        sleep(2)
        # scrolled1.location_once_scrolled_into_view
        # tasks_list.enter_customer_manager_date_filter(a)
        # tasks_list.enter_customer_manager_date_filter_btn()
        tasks_list.enter_customer_manager_my_tasks_click_auto_need_pick_up_order()
        sleep(2)
        tasks_list.enter_customer_manager_my_tasks_page_auto_need_pick_up_order()
        message = "با موفقیت وارد قسمت دستور بارگیری شد. "
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    ################### box_pickup_check ###################

    def test18_box_pickup_check(self):
        self.driver.implicitly_wait(10)
        # self.driver.maximize_window()
        box_pickup = Box_Pickup(driver=self.driver)
        # box_pickup.enter_click_cargo_pickup()
        box_pickup.enter_box_pickup_check_order_check()
        box_pickup.enter_box_pickup_check_order()
        box_pickup.enter_box_pickup_check_internal_carriage()
        box_pickup.enter_box_pickup_sender_information()
        self.tests_texts.append("بخش های مختلف تاییدیه فاکتور بررسی شد. ")
        print("############################################")

    ################### box_pickup_send_pickup_command ###################

    def test19_box_pickup_send_pickup_command(self):
        self.driver.implicitly_wait(10)
        box_pickup = Box_Pickup(driver=self.driver)
        # box_pickup.enter_box_pickup_send_the_pickup_command()
        # sleep(5)
        # box_pickup.enter_box_pickup_send_the_pickup_command_error()
        box_pickup.enter_box_pickup_sender_person()
        box_pickup.enter_box_pickup_sender_person_name("ملیکا کابلی")
        sleep(3)
        box_pickup.enter_box_pickup_sender_person_option()
        box_pickup.enter_box_pickup_sender_company()
        box_pickup.enter_box_pickup_sender_company_name("فاطر")
        sleep(1)
        box_pickup.enter_box_pickup_sender_company_option()
        box_pickup.enter_box_pickup_sender_submit()
        print("اطلاعات فرستنده ثبت شد. ")
        box_pickup.enter_box_pickup_send_the_pickup_command()
        box_pickup.enter_box_pickup_cancel_the_download_order()
        box_pickup.enter_box_pickup_send_the_pickup_command()
        print(" دستور بارگیری ارسال شد. ")
        self.tests_texts.append("اطلاعات فرستنده ثبت و دستور بارگیری ارسال شد. ")
        print("############################################")

    ################### login_warehouses ###################

    def test20_login_warehouses(self):
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        sleep(.5)
        login.enter_login_username(warehouse_id)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        message = "با موفقیت وارد پنل انبار دار شد"
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    ################### Warehouses ###################

    def test21_Warehouses(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        sleep(.3)
        # orders_create.enter_click_feather_light_content()
        tasks_list.enter_customer_manager_my_tasks()
        sleep(.5)
        self.driver.refresh()
        sleep(1)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.3)
        # orders_create.enter_click_feather_light_content()
        print("وارد انبار چین شدید.")
        warehouses.enter_warehouses_goods_loading_list()
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_search("")
        warehouses.enter_warehouses_goods_loading_list_update()
        warehouses.enter_warehouses_goods_loading_list_order_loading_status()
        warehouses.enter_warehouses_goods_loading_list_order_loading_status_option()
        warehouses.enter_warehouses_goods_loading_list_order_loading_status_update()
        message = " وضعیت سفارش به تماس گرفته شده و پاسخ داده نشده تغییر پیدا کرد."
        print(message)
        self.tests_texts.append(message)
        ROOT_DIR = os.path.abspath(os.altsep)
        # print(ROOT_DIR)
        print("############################################")

    ################### called_and_not_answered ###################

    def test22_called_and_not_answered(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_warehouses_goods_loading_list_called_and_not_answered()
        print("وراد قسمت تماس گرفته شده و پاسخ داده نشده شدید.")
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_update()
        warehouses.enter_warehouses_goods_loading_list_order_loading_status()
        warehouses.enter_warehouses_goods_loading_list_order_loading_status_option2()
        warehouses.enter_warehouses_goods_loading_list_order_loading_status_update()
        message = " وضعیت سفارش به در حال ارسال به انبار تغییر پیدا کرد."
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    ################### on_the_way ###################

    def test23_on_the_way(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_warehouses_goods_loading_list_click_on_the_way()
        print("وراد قسمت در حال ارسال به انبار شدید.")
        warehouses.enter_warehouses_goods_loading_list_cargo_pickup()
        warehouses.enter_warehouses_goods_loading_list_total_qty("2")
        warehouses.enter_warehouses_goods_loading_list_total_qty_update()
        print("به قسمت افزودن کالا برای بارگیری وارد شدید.")
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2()
        sleep(1)
        # warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_list()
        scrolled1 = self.driver.find_element('xpath', "//*[@id='oppickup']/button")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print(" برای ذخیره وارد کردن دیتا الزامی می باشد.")
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_data()
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print(" برای ذخیره تصویر بیرونی کالا الزامی می باشد.")
        sleep(1)
        # print(ROOT_DIR)
        # self.driver.find_element('xpath', warehouses_goods_loading_list_pickup_add1_from2_exterior_image).send_keys(ROOT_DIR + "\\box.jpg")
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_exterior_image()
        sleep(0.3)
        scrolled1.location_once_scrolled_into_view
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print(" برای ذخیره تصویر درونی کالا الزامی می باشد.")
        sleep(.5)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_internal_image()
        sleep(.2)
        scrolled1.location_once_scrolled_into_view
        sleep(.2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_no_form_print()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        sleep(5)
        # all_handle1 = self.driver.window_handles
        # le1 = len(self.driver.window_handles)
        # self.driver.switch_to.window(all_handle1[le1-1])
        # self.driver.back()
        # self.driver.close()
        # window_handles = driver.window_handles
        # driver.switch_to.window(window_handles[-1])
        # self.driver.close()
        # self.driver.back()
        print("برچسب کالا اضافه شد.")
        sleep(2)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2()
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_list2()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_data2()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_exterior_image()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_internal_image()
        sleep(0.3)
        scrolled2 = self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[2]/div/div/form/div[4]/div/label")
        sleep(.2)
        scrolled2.location_once_scrolled_into_view
        sleep(.2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_no_form_print()
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2_update()
        print("برچسب کالا اضافه شد.")
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_check_disabled_add()
        warehouses.enter_warehouses_goods_loading_list_pickup_check_add_barcode()
        warehouses.enter_warehouses_goods_loading_list_pickup_add_warehouses()
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_pickup_success_add()
        sleep(1)
        self.tests_texts.append("برچسب های کالا اضافه شد.")
        print("############################################")

    ################### check_no_batch ###################

    def test24_check_no_batch(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_warehouses_show_order_id()
        el = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[1]/h1/a[1]/span").text
        result = el.replace("سفارش", "")
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.3)
        warehouses.enter_warehouses_orders_in_warehouse()
        warehouses.enter_warehouses_orders_in_warehouse_search(result)
        warehouses.enter_warehouses_orders_in_warehouse_order_id()
        warehouses.enter_warehouses_orders_in_warehouse_check_allow_batching()
        self.tests_texts.append("اجازه بچ کردن بررسی شد.")
        print("############################################")

    ################### Login_clearance ###################

    def test25_login_clearance(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[2]/a[1]").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        login.enter_login_username(account_clearance)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد")
        my_tasks.enter_clearance_my_tasks()
        my_tasks.enter_clearance_my_tasks_need_final_clearance()
        print("وارد قسمت نیاز به استعلام ترخیص نهایی شد.")
        self.tests_texts.append("با موفقیت وارد پنل مدیر واحد استعلام ترخیص و قسمت نیاز به استعلام ترخیص نهایی شد. ")
        my_tasks.enter_clearance_my_tasks_update()
        sleep(2)
        my_tasks.enter_clearance_my_tasks_search(a)
        sleep(1)
        my_tasks.enter_clearance_my_tasks_search_btn()
        print("############################################")

    ################### clearance_my_tasks_final_clearance #########################

    def test26_my_tasks_final_clearance(self):
        self.driver.implicitly_wait(10)
        my_tasks = My_Tasks(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        my_tasks.enter_clearance_my_tasks_final_clearance()
        sleep(1)
        a = self.driver.find_element('xpath', "/html/body/div[7]/div/div/div/section[1]/h1/a/span").text
        print(a)
        my_tasks.enter_clearance_my_tasks_final_clearance_text_issue()
        scrolled = self.driver.find_element('xpath', clearance_my_tasks_final_clearance_loaded_goods)
        scrolled.location_once_scrolled_into_view
        my_tasks.enter_clearance_my_tasks_final_clearance_loaded_goods()
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval_error()
        my_tasks.enter_clearance_my_tasks_final_clearance_record_the_value_of_goods()
        my_tasks.enter_clearance_my_tasks_final_clearance_record_the_value("2000")
        my_tasks.enter_clearance_my_tasks_final_clearance_record_the_value_send()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval()
        my_tasks.enter_clearance_my_tasks_final_clearance_checkbox_order()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_final_clearance_category()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_final_clearance_category_option()
        my_tasks.enter_clearance_my_tasks_final_clearance_category_send()
        my_tasks.enter_clearance_my_tasks_final_clearance_customs_approval()
        my_tasks.enter_clearance_my_tasks()
        my_tasks.enter_clearance_my_tasks_need_final_clearance()
        my_tasks.enter_clearance_my_tasks_update()
        sleep(2)
        my_tasks.enter_clearance_my_tasks_search(a)
        my_tasks.enter_clearance_my_tasks_search_btn()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_final_clearance()
        sleep(1)
        scrolled2 = self.driver.find_element('xpath', clearance_my_tasks_need_to_issue_price)
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        my_tasks.enter_clearance_my_tasks_need_to_issue_price(2000000)
        my_tasks.enter_clearance_my_tasks_need_to_issue_price_unit()
        sleep(0.3)
        my_tasks.enter_clearance_my_tasks_need_to_issue_price_unit_option()
        sleep(1)
        scrolled3 = self.driver.find_element('xpath', clearance_my_tasks_need_to_issue_btn)
        sleep(1)
        scrolled3.location_once_scrolled_into_view
        sleep(1)
        my_tasks.enter_clearance_my_tasks_need_to_issue_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        message = "پیش فاکتور نهایی صادر شد. "
        print(message)
        self.tests_texts.append(message)
        scrolled4 = self.driver.find_element('xpath', clearance_my_tasks_search)
        sleep(.5)
        scrolled4.location_once_scrolled_into_view
        sleep(1)
        print("############################################")

    ################### clearance_my_tasks_final_clearance #########################

    def test27_login_customer_manager(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div[3]/div/table/tbody/tr/td[5]/a[1]").text
        print(a)
        self.driver.get(base_url)
        tasks_list = Tasks_list(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        message = "با موفقیت وارد پنل مدیر مشتری شد"
        print(message)
        self.tests_texts.append(message)
        sleep(.3)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        print("############################################")

    def test28_my_tasks_final_clearance(self):
        self.driver.implicitly_wait(10)
        sleep(3)
        a = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div[3]/div/div/div/div[3]/div/table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        tasks_list = Tasks_list(driver=self.driver)
        sleep(0.5)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_to_customer()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter("")
        # tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        # sleep(2)
        driver.implicitly_wait(10)
        try:
            tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        except:
            sleep(0.5)

        # tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        # sleep(1)
        # driver.set_window_size(480, 640)
        sleep(1)
        # all_handle = self.driver.window_handles
        # sleep(1)
        # self.driver.switch_to.window(all_handle[3])
        # sleep(1)
        sleep(1)
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[9]/div[2]/a[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer()
        print("فاکتور حمل به مشتری ارسال شد. ")
        sleep(2)
        # scrolled2 = self.driver.find_element('xpath',
        #                                      "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[9]/div[2]/a[1]")
        # sleep(1)
        # scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance_not_sent_to_the_customer()
        print("فاکتور ترخیص به مشتری ارسال شد. ")
        tasks_list.enter_customer_manager_my_tasks()
        # self.driver.refresh()
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer()
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(a)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_send_invoice_clearance()
        sleep(1)
        all_handle1 = self.driver.window_handles
        sleep(1)
        self.driver.switch_to.window(all_handle1[4])
        sleep(1)
        scrolled3 = self.driver.find_element('xpath',
                                             "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[9]/div[3]/a[1]")
        sleep(1)
        scrolled3.location_once_scrolled_into_view
        sleep(.4)
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_approval()
        print("فاکتور حمل توسط مشتری تایید شد. ")
        sleep(1)
        # scrolled4 = self.driver.find_element('xpath',
        #                                      "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[2]/td[9]/div[2]/a[1]")
        # sleep(1)
        # scrolled4.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_no_customer_approval()
        print("فاکتور ترخیص توسط مشتری تایید شد. ")
        self.tests_texts.append("فاکتور ها به درستری برای مشتری ارسال و تایید شدند. ")
        print("############################################")

    ################### auto_need_shipping #########################

    def test29_auto_need_shipping(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[1]/h1/a[1]/span").text
        print(a)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_auto_need_shipping()
        sleep(1)
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_click_need_shipping()
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_need_shipping_form_approvals_text)
        scrolled1.location_once_scrolled_into_view
        # tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_text("12345678")
        # tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_send()
        # clearance_inquery.enter_click_alert()
        # print("تعداد کاراکتر ها کمتر از 10 می باشد. ")
        # scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_text(
            "این توضیحات تست تاییدیه برای حمل بین الملل می باشد. ")
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_send()
        tasks_list.enter_customer_manager_my_tasks_warehouses()
        tasks_list.enter_customer_manager_my_tasks_warehouses_need_to_batch()
        message = "وارد تب انبار و سفارشات در انتظار بچ شد. "
        print(message)
        self.tests_texts.append(message)
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter(a)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        print("############################################")

    ################### login_warehouses ###################

    def test30_login_warehouses(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', customer_manager_date_filter).text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        sleep(1)
        login.enter_login_username(warehouse_id)
        sleep(.3)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل انبار دار شد")
        tasks_list.enter_customer_manager_my_tasks()
        self.driver.refresh()
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.3)
        print("وارد انبار چین شدید.")
        warehouses.enter_warehouses_create_batch()
        warehouses.enter_warehouses_create_batch_destination("Iran-Tehran-Customs-IKA" + Keys.ENTER)
        warehouses.enter_warehouses_create_batch_send()
        all_handle1 = self.driver.window_handles
        le1 = len(self.driver.window_handles)
        self.driver.switch_to.window(all_handle1[le1-1])
        sleep(1)
        batch_name = warehouses.enter_warehouses_create_batch_name()
        print(batch_name)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_orders_in_warehouse()
        sleep(.3)
        warehouses.enter_warehouses_orders_in_warehouse_search(a)
        # warehouses.enter_warehouses_orders_in_warehouse_search("")
        print("############################################")

        ################### warehouses_orders_in_warehouse_check ###################

        # def test31_warehouses_orders_in_warehouse_check(self):
        #     self.driver.implicitly_wait(10)
        #     warehouses = Warehouses(driver=self.driver)
        #     a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_order_id).text
        #     print(a)
        #     warehouses.enter_warehouses_orders_in_warehouse_search(a)
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_check_count()
        warehouses.enter_warehouses_orders_in_warehouse_check_weight()
        warehouses.enter_warehouses_orders_in_warehouse_check_allow_batching_yes()
        print("############################################")

        ################### warehouses_orders_in_warehouse_create_batch ###################

        # def test32_warehouses_orders_in_warehouse_create_batch(self):
        #     self.driver.implicitly_wait(10)
        #     warehouses = Warehouses(driver=self.driver)
        #     a = self.driver.find_element('xpath', warehouses_orders_in_warehouse_check_order_id).text
        #     print(a)
        #     warehouses.enter_warehouses_orders_in_warehouse_search(a)
        #     sleep(1)
        # warehouses.enter_warehouses_orders_in_warehouse_check_count()
        # warehouses.enter_warehouses_orders_in_warehouse_check_weight()
        # warehouses.enter_warehouses_orders_in_warehouse_check_allow_batching_yes()
        # sleep(.3)
        warehouses.enter_warehouses_orders_in_warehouse_click_order_id()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_click_checkbox1()
        warehouses.enter_warehouses_orders_in_warehouse_click_checkbox2()
        # warehouses.enter_warehouses_orders_in_warehouse_click_create_new_batch()
        sleep(1)
        # warehouses.enter_warehouses_orders_in_warehouse_assert_create_new_batch()/
        sleep(.2)
        # warehouses.enter_warehouses_orders_in_warehouse_closed_tab_click_batch()
        # sleep(1)
        # warehouses.enter_warehouses_orders_in_warehouse_search(a)
        # sleep(1)
        # warehouses.enter_warehouses_orders_in_warehouse_click_order_id()
        # sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_select_batch(batch_name)
        ### warehouses.enter_warehouses_orders_in_warehouse_select_batch_option()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_select_batch_btn()
        # warehouses.enter_warehouses_orders_in_warehouse_assert_create_add_batch()
        sleep(5)
        warehouses.enter_warehouses_orders_in_warehouse_click_batch()
        sleep(2)
        warehouses.enter_warehouses_orders_in_warehouse_check_form_batch()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_batch_check_order1()
        warehouses.enter_warehouses_orders_in_warehouse_batch_check_order2()
        # warehouses.enter_warehouses_orders_in_warehouse_replace_name_batch()
        # warehouses.enter_warehouses_orders_in_warehouse_update_name_batch()
        print("باید برای خروج از انبار مقصد را تعیین کنیم.")
        # warehouses.enter_warehouses_orders_in_warehouse_select_destination_batch()
        # warehouses.enter_warehouses_orders_in_warehouse_select_option_destination_batch()
        warehouses.enter_warehouses_orders_in_warehouse_closed_batch()
        warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        warehouses.enter_warehouses_orders_in_warehouse_waybill_number_batch("12345")
        # warehouses.enter_warehouses_orders_in_warehouse_closed_batch()
        # warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        # print("باید برای خروج از انبار مقصد را تعیین کنیم.")
        # warehouses.enter_warehouses_orders_in_warehouse_select_destination_batch()
        # warehouses.enter_warehouses_orders_in_warehouse_select_option_destination_batch()
        # warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        warehouses.enter_warehouses_orders_in_warehouse_batch_shipping_international()
        self.tests_texts.append("بچ کردن انجام و بررسی شد. ")
        print("############################################")

    ################### Login_clearance_inquery ###################

    def test31_login_clearance(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
        a = warehouses.enter_warehouses_orders_in_warehouse_batch_show_number()
        op_id1 = warehouses.enter_warehouses_orders_in_warehouse_batch_show_op_id1()
        op_id2 = warehouses.enter_warehouses_orders_in_warehouse_batch_show_op_id2()
        # a = "2273CIN"
        # op_id1 = "425693"
        # op_id2 = "425695"
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
        sleep(1)
        my_tasks.enter_clearance_my_tasks_update()
        sleep(3)
        my_tasks.enter_clearance_my_tasks_search(a)
        my_tasks.enter_clearance_my_tasks_search_btn()
        sleep(1)
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_click_batch()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_edite()
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_declared_value("100")
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_btn()
        sleep(2)
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
        sleep(1)
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id_btn()
        sleep(1)
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_check_declared_value()
        sleep(1)
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_price("110")
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_price_btn()
        sleep(2)
        my_tasks.enter_clearance_warehouses_psp_evaluation_of_goods_received_price_msg()
        self.tests_texts.append("کالا در مقصد دریافت و ارزش گذاری شد. ")
        print("############################################")

    ################### Login_customer_manager ###################

    def test32_login_customer_manager(self):
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
        message = "با موفقیت وارد پنل مدیر مشتری شد"
        print(message)
        self.tests_texts.append(message)
        sleep(.3)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call()
        sleep(1)
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(0.5)
        print("############################################")

    ################### my_tasks_op_delivery_call ###################

    def test33_my_tasks_op_delivery_call(self):
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
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option()
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_text_mali_fake("این توضیحات مالی تستی می باشد.")
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
        sleep(.3)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location("تست توضیحات عدم ثبت لوکیشن")
        sleep(.4)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
        # delivery.enter_delivery_manager_allocation_map_zoom_out2()
        # sleep(3)
        # delivery.enter_delivery_manager_allocation_map_click()
        # sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        print("پیش فاکتور های سفارش فاقد صاحب پیش فاکتور ی باشند. لطفا خطاها را اصلاح کنید.")
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(3)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_closed()
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(a)
        tasks_list.enter_customer_manager_date_filter_btn()
        self.tests_texts.append("برای هماهنگی با مشتتری ابتدا باید خطاها را اصلاح کنیم. ")
        print("############################################")

    ################### my_tasks_op_delivery_call ###################

    def test34_my_tasks_op_delivery_call(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_click_order()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_text("ملیکا کابلی")
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_company()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_company_text("ملیکا کابلی")
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_company_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_error()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_text("ملیکا کابلی")
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_person_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_change_pro_invoice_confirmation()
        sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_box_invoices_update_exchange()
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call()
        sleep(1)
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        sleep(2)
        tasks_list.enter_customer_manager_date_filter(a)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(1)
        self.tests_texts.append("پیش فاکتور ها آپدیت شدند. ")
        print("############################################")

    ################### my_tasks_op_delivery_call_confirmation ###################

    def test35_my_tasks_op_delivery_call_confirmation(self):
        self.driver.implicitly_wait(10)
        # scrolled = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]")
        # sleep(.4)
        # scrolled.location_once_scrolled_into_view
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        tasks_list = Tasks_list(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_click()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_clearing_type_fake_option()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake()
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option()
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_text_mali_fake("این توضیحات مالی تستی می باشد.")
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_date)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        sleep(1)
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
        sleep(.3)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location("تست توضیحات عدم ثبت لوکیشن")
        sleep(.4)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
        delivery.enter_delivery_manager_allocation_map_zoom_out2()
        sleep(3)
        delivery.enter_delivery_manager_allocation_map_click()
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        sleep(1)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location("تست توضیحات عدم ثبت لوکیشن")
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        sleep(3)
        clearance_inquery.enter_click_alert()
        sleep(3)
        clearance_inquery.enter_click_alert()
        sleep(3)
        clearance_inquery.enter_click_alert()
        # sleep(.4)
        # scrolled2.location_once_scrolled_into_view
        # sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
        # sleep(.4)
        # scrolled2.location_once_scrolled_into_view
        # sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        sleep(1)
        # clearance_inquery.enter_click_alert()
        message ="هماهنگی ثبت شد. "
        print(message)
        self.tests_texts.append(message)
        sleep(2)
        clearance_inquery.enter_click_alert()
        print("############################################")

    ################### login_Financial_Manager ###################

    def test36_login_financial_manager(self):
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
        message = "با موفقیت وارد پنل مدیر مالی شد. "
        print(message)
        self.tests_texts.append(message)
        financial.enter_financial_my_tasks()
        financial.enter_financial_my_tasks_need_official_invoice()
        sleep(1)
        financial.enter_financial_update_my_tasks()
        sleep(1)
        financial.enter_financial_search(b)
        sleep(1)
        financial.enter_financial_search_btn()
        print("############################################")

    ################### my_tasks_need_official_invoice ###################

    def test37_my_tasks_need_official_invoice(self):
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
        sleep(3)
        clearance_inquery.enter_click_alert()
        sleep(2)
        clearance_inquery.enter_click_alert()
        sleep(2)
        clearance_inquery.enter_click_alert()
        sleep(3)
        clearance_inquery.enter_click_alert()
        sleep(3)
        clearance_inquery.enter_click_alert()
        sleep(2)
        clearance_inquery.enter_click_alert()
        sleep(2)
        clearance_inquery.enter_click_alert()
        # financial.enter_financial_my_tasks_need_official_invoice_click_order()
        print("############################################")
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        # delivery = Delivery_Manager(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        message = "با موفقیت وارد پنل مدیر دلیوری شد. "
        print(message)
        self.tests_texts.append(message)
        print("############################################")
        delivery.enter_my_task_delivery_manager()
        delivery.enter_delivery_manager_my_task_all()
        delivery.enter_delivery_manager_my_task_determine_drive()
        delivery.enter_delivery_manager_my_task_update()
        sleep(1)
        delivery.enter_delivery_manager_my_task_search(a)
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()

    ################### login_delivery_manager ###################

    def test38_delivery_manager(self):
        self.driver.implicitly_wait(10)
        # # a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        # # print(a)
        # self.driver.get(base_url)
        # login = LoginPage(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        # # delivery = Delivery_Manager(driver=self.driver)
        # login.enter_login_username(delivery_manager)
        # login.enter_login_btn_submit_next()
        # login.enter_login_password(code_no_admin)
        # login.enter_login_btn_submit()
        # print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        # delivery.enter_my_task_delivery_manager()
        # # sleep(.5)
        # delivery.enter_delivery_manager_my_task_all()
        # delivery.enter_delivery_manager_my_task_determine_drive()
        # delivery.enter_delivery_manager_my_task_update()
        # sleep(1)
        # delivery.enter_delivery_manager_my_task_search("")
        # sleep(1)
        # delivery.enter_delivery_manager_my_task_search_btn()
        b = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
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
        message = "با موفقیت راننده اختصاص داده شد. "
        print(message)
        self.tests_texts.append(message)
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()
        print("############################################")

    ################### login_delivery ###################

    def test39_delivery(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        persons = Persons(driver=self.driver)
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
        delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_text(
            "توضیحات تاییدیه دریافت شده توسط راننده")
        delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder()
        print("تاییدیه دریافت شده توسط راننده انجام شد. ")
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer()
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn()
        print("باید امضا را اضافه کنید. ")
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_choose_file()
        delivery.enter_delivery_my_task_deliver_to_customer_ready_deliver_to_customer_btn()
        sleep(1)
        clearance_inquery.enter_click_alert()
        sleep(1)
        clearance_inquery.enter_click_alert()

        ################### Login_customer_manager ###################

        self.driver.get(base_url)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        persons.enter_psp_search_select()
        persons.enter_psp_search_select_name(a)
        persons.enter_psp_search_select_option()
        delivery.enter_delivery_order_delivered_assert()
        message = "تست با موفقیت به پایان رسید. "
        print(message)
        self.tests_texts.append(message)
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_main, 'Main')
