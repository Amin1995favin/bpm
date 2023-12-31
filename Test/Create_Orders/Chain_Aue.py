from selenium import webdriver
from selenium.webdriver import Keys
from time import sleep
from Locators import *
from Pages.Clearance.My_Tasks import My_Tasks
from Pages.Clearance_Inquery import Clearance_Inquery
from Pages.Customer_Manager.Box_Pickup import Box_Pickup
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Delivery_Manager.Delivery_Manager import Delivery
from Pages.Financial_Manager.financial_manager import Financial_Manager
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
from Pages.Find_Element import FindElement
import unittest
from Pages.Persons import Persons
from Pages.Warehouses.Warehouses import Warehouses
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)


class Test_bpm(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.tests_texts = []

    ################### Login_customer_manager ###################

    def test01_login_customer_manager(self):
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
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
        print("وارد قسمت انتخاب خدمات مورد نیاز شد.")
        print("############################################")

    ################### orders_create_products ###################

    def test03_orders_create_products(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_click_create_order_product()
        scrolled2 = self.driver.find_element('xpath', orders_create_category_select)
        scrolled2.location_once_scrolled_into_view
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        orders_create.enter_orders_create_detailed_classification_of_goods()
        sleep(1)
        orders_create.enter_orders_create_detailed_classification_of_goods_option()
        scrolled1 = self.driver.find_element('xpath', orders_create_submit_information)
        print("با انتخاب فقط دسته بندی کلی کالا نمی توان به مرحله بعد رفت.")
        orders_create.enter_orders_create_form_name_en("دوربین")
        print("نام انگلیسی کالا بصورت انگلیسی وارد نشده است.")
        orders_create.enter_orders_create_form_name_en("camera")
        orders_create.enter_orders_create_form_type()
        orders_create.enter_orders_create_form_type_option()
        print("باید تعداد وارد شود.")
        orders_create.enter_orders_create_form_quantity_number("1000")
        print("باید وزن واحد وارد شود.")
        orders_create.enter_orders_create_form_one_weight("1")
        scrolled1.location_once_scrolled_into_view
        orders_create.enter_orders_create_submit_information()
        sleep(1)
        print("با موفقیت تکمیل اطلاعات سفارش انجام شد.")
        sleep(3)
        orders_create.enter_create_order_product_check_passed()
        print("############################################")

    def test04_orders_create_products(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        findel = FindElement(driver=self.driver)
        orders_create.enter_click_create_order_product()
        orders_create.enter_orders_create_category_select()
        orders_create.enter_orders_create_category_select_option()
        orders_create.enter_orders_create_detailed_classification_of_goods()
        sleep(.5)
        orders_create.enter_orders_create_detailed_classification_of_goods_option()
        orders_create.enter_orders_create_form_name("دوربین2")
        orders_create.enter_orders_create_form_name_en("camera2")
        orders_create.enter_orders_create_form_type()
        orders_create.enter_orders_create_form_type_option()
        orders_create.enter_orders_create_form_quantity()
        orders_create.enter_orders_create_form_quantity_option()
        orders_create.enter_orders_create_form_quantity_number("20")
        orders_create.enter_orders_create_form_one_weight("2")
        findel.wait_until_element_has_an_attribute_and_send('xpath', orders_create_form_length, 'name', '2', 'length')
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
        print("############################################")

    ################### orders_create_products_check_price_unit ###################

    def test05_orders_create_products_check_price_unit(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_sender_city_btn2("Shenzhen - China")
        sleep(0.7)
        orders_create.enter_orders_create_sender_person("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_check_receiver_city_btn2("Dubai")
        sleep(0.7)
        orders_create.enter_orders_create_receiver_person("ملیکا کابلی")
        orders_create.enter_orders_create_information_factor_rasmi_transport()
        orders_create.enter_orders_create_information_factor_rasmi_transport_option()
        orders_create.enter_orders_create_information_factor_rasmi_clearance()
        orders_create.enter_orders_create_information_factor_rasmi_clearance_option()
        orders_create.enter_orders_create_information_factor_rasmi()
        orders_create.enter_orders_create_information_factor_rasmi_option()
        orders_create.enter_orders_create_information_approve()
        sleep(1)
        orders_create.enter_create_order_product_check_all_data2()
        # ________________________________________________________________
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_check_color_checking_the_order()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_product_details_of_this_order_are_approved()
        sleep(1)
        print("############################################")

    def test06_review_and_correct_order(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        orders_create.enter_click_other_inquiries()
        orders_create.enter_click_other_inquiries_check()
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[9]/div[2]/a[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer()
        self.driver.refresh()
        print("فاکتور حمل به مشتری ارسال شد. ")
        scrolled2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr/td[9]/div[3]/a[1]")
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_approval()
        print("فاکتور حمل توسط مشتری تایید شد. ")
        print("############################################")

    ################### box_pickup_send_pickup_command ###################

    def test07_box_pickup_send_pickup_command(self):
        self.driver.implicitly_wait(10)
        box_pickup = Box_Pickup(driver=self.driver)
        sleep(1)
        scrolled = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div[12]/a")
        sleep(1)
        scrolled.location_once_scrolled_into_view
        sleep(1)
        self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/div[2]/div[9]/a").click()
        box_pickup.enter_box_pickup_sender_submit()
        print("اطلاعات فرستنده ثبت شد. ")
        box_pickup.enter_box_pickup_send_the_pickup_command()
        box_pickup.enter_box_pickup_cancel_the_download_order()
        box_pickup.enter_box_pickup_send_the_pickup_command()
        print(" دستور بارگیری ارسال شد. ")
        print("############################################")

    ################### login_warehouses ###################

    def test08_login_warehouses(self):
        a = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a[1]/span").text
        print(a)
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        sleep(.5)
        login.enter_login_username(warehouse_id)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل انبار دار شد")
        print("############################################")
        tasks_list.enter_customer_manager_my_tasks()
        self.driver.refresh()
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.1)
        # orders_create.enter_click_feather_light_content()
        print("وارد انبار چین شدید.")
        warehouses.enter_warehouses_goods_loading_list()
        sleep(1)
        warehouses.enter_warehouses_goods_loading_list_search(a)

    ################### Warehouses ###################

    def test09_Warehouses(self):
        self.driver.implicitly_wait(10)
        tasks_list = Tasks_list(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        warehouses.enter_warehouses_china_click_tn()
        warehouses.enter_warehouses_china_check_cargo_pickup()
        warehouses.enter_warehouses_china_click_cargo_pickup()
        warehouses.enter_warehouses_china_click_pickup()
        print("به مرحله چاپ برچسب برای بارگیری وارد شد.")
        print("############################################")

    ################### on_the_way ###################

    def test10_on_the_way(self):
        self.driver.implicitly_wait(10)
        warehouses = Warehouses(driver=self.driver)
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
        sleep(0.1)
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
        sleep(1)
        print("برچسب کالا اضافه شد.")
        sleep(2)
        warehouses.enter_warehouses_goods_loading_list_pickup_add1_from2()
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
        sleep(.1)
        warehouses.enter_warehouses_goods_loading_list_pickup_success_add()
        sleep(.1)
        warehouses.enter_warehouses_show_order_id()
        print("############################################")

    ################### Login_customer_manager ###################

    def test11_login_customer_manager(self):
        el = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[1]/h1/a[1]/span").text
        result = el.replace("سفارش", "")
        self.driver.get(base_url)
        orders_create = Orders_Create(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        orders_create.enter_search_tn(result)
        sleep(1)
        orders_create.enter_click_box_invoices()

    def test12_review_and_correct_order(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        scrolled1 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr[1]/td[9]/div[2]/a[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer()
        self.driver.refresh()
        print("فاکتور حمل به مشتری ارسال شد. ")
        scrolled2 = self.driver.find_element('xpath', "/html/body/div[1]/div[1]/section[2]/div/div[2]/div/div[2]/div/table/tbody/tr/td[9]/div[3]/a[1]")
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_approval()
        print("فاکتور حمل توسط مشتری تایید شد. ")
        self.driver.refresh()
        scrolled2 = self.driver.find_element('xpath', customer_manager_my_tasks_need_shipping_form_approvals_text)
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_text("این توضیحات تست تاییدیه برای حمل بین الملل می باشد. ")
        tasks_list.enter_customer_manager_my_tasks_need_shipping_form_approvals_send()
        print("############################################")

    ################### login_warehouses ###################

    def test13_login_warehouses(self):
        a = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a[1]/span").text
        print(a)
        self.driver.implicitly_wait(10)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        sleep(.5)
        login.enter_login_username(warehouse_id)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل انبار دار شد")
        print("############################################")
        tasks_list.enter_customer_manager_my_tasks()
        self.driver.refresh()
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        sleep(0.1)
        print("وارد انبار چین شدید.")
        warehouses.enter_warehouses_create_batch()
        warehouses.enter_warehouses_create_batch_destination("Dubai WH" + Keys.ENTER)
        warehouses.enter_warehouses_create_batch_send()
        sleep(1)
        all_handle1 = self.driver.window_handles
        self.driver.switch_to.window(all_handle1[1])
        sleep(1)
        batch_name = warehouses.enter_warehouses_create_batch_name()
        print(batch_name)
        warehouses.enter_click_warehouses()
        warehouses.enter_click_warehouse_china()
        warehouses.enter_warehouses_orders_in_warehouse()
        sleep(.3)
        warehouses.enter_warehouses_orders_in_warehouse_search(a)

        ################### warehouses_orders_in_warehouse_batch ###################

        warehouses.enter_warehouses_orders_in_warehouse_check_count()
        warehouses.enter_warehouses_orders_in_warehouse_check_weight()
        warehouses.enter_warehouses_orders_in_warehouse_check_allow_batching_yes()
        warehouses.enter_warehouses_orders_in_warehouse_click_order_id()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_click_checkbox1_aue()
        warehouses.enter_warehouses_orders_in_warehouse_click_checkbox2_aue()
        warehouses.enter_warehouses_orders_in_warehouse_select_batch(batch_name)
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_select_batch_btn()
        sleep(5)
        warehouses.enter_warehouses_orders_in_warehouse_click_batch()
        sleep(2)
        warehouses.enter_warehouses_orders_in_warehouse_check_form_batch()
        sleep(1)
        print("باید برای خروج از انبار مقصد را تعیین کنیم.")
        warehouses.enter_warehouses_orders_in_warehouse_closed_batch()
        warehouses.enter_warehouses_orders_in_warehouse_exiting_and_sending_batch()
        warehouses.enter_warehouses_orders_in_warehouse_waybill_number_batch("12345")
        warehouses.enter_warehouses_orders_in_warehouse_batch_shipping_international()
        sleep(1)
        warehouses.enter_warehouses_orders_in_warehouse_batch_shipping_international()
        print("############################################")

    ################### Login_clearance_inquery ###################

    def test14_login_clearance(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        warehouses = Warehouses(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        a = warehouses.enter_warehouses_orders_in_warehouse_batch_show_number()
        tn = warehouses.enter_warehouses_orders_in_warehouse_batch_show_tn()
        op_id1 = warehouses.enter_warehouses_orders_in_warehouse_batch_show_op_id1()
        op_id2 = warehouses.enter_warehouses_orders_in_warehouse_batch_show_op_id2()
        print(a)
        print(tn)
        print(op_id1)
        print(op_id2)
        self.driver.get(base_url)
        my_tasks = My_Tasks(driver=self.driver)
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_uae)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص دبی شد")
        print("############################################")
        my_tasks.enter_clearance_my_tasks_notification_closure_batch_manifests_dubai(a)
        sleep(1)
        my_tasks.enter_clearance_warehouses_dubai()
        my_tasks.enter_clearance_warehouses_dubai_receive_confirm_box()
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id(op_id1)
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id_btn()
        sleep(1)
        self.driver.refresh()
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id(op_id2)
        my_tasks.enter_clearance_warehouses_psp_receipt_confirmation_op_id_btn()
        sleep(1)
        self.driver.refresh()
        orders_create.enter_search_tn(tn)
        orders_create.enter_click_box_op()
        orders_create.enter_check_op_in_warehouses()
        # self.driver.back()
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.enter_customer_manager_my_tasks_notify_order_in_dubai_batch()
        sleep(1)
        tasks_list.enter_customer_manager_update_my_tasks()
        sleep(1)
        tasks_list.enter_customer_manager_date_filter(tn)
        sleep(1)
        tasks_list.enter_customer_manager_date_filter_btn()
        sleep(0.5)
        tasks_list.enter_customer_manager_my_tasks_notify_order_in_dubai_batch_submit()
        sleep(1)

    ################### Login_customer_manager ###################

    def test15_login_customer_manager(self):
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]//a[1]").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        login.enter_login_username(account_customer_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری شد")
        print("############################################")
        sleep(.1)
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

    def test16_my_tasks_op_delivery_call(self):
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
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_send_invoice_fake_option2()
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_text_mali_fake("این توضیحات مالی تستی می باشد.")
        scrolled1 = self.driver.find_element('xpath', customer_manager_my_tasks_op_delivery_call_date)
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_date("۱۴۰۲/۱۲/۲۰")
        sleep(.3)
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_name("کاربر تست")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile("0")
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile_error()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_mobile("989124455666")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone("0")
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone_error()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_phone("982155667788")
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_delivery_type()
        # sleep(1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_delivery_type_option()
        scrolled2 = self.driver.find_element('xpath', "//button[text()=' ثبت اطلاعات']")
        sleep(.4)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        sleep(.1)
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_descnotreg_location(
        #     "تست توضیحات عدم ثبت لوکیشن")
        # sleep(.4)
        # scrolled2.location_once_scrolled_into_view
        # tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_btn()
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address("تهران")
        tasks_list.enter_customer_manager_my_tasks_op_delivery_call_form_address2("تهران")
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
        print("############################################")

    ################### login_delivery ###################

    def test17_delivery(self):
        self.driver.implicitly_wait(10)
        a = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[5]/a[1]").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        persons = Persons(driver=self.driver)
        clearance_inquery = Clearance_Inquery(driver=self.driver)
        delivery = Delivery(driver=self.driver)
        # delivery = Delivery_Manager(driver=self.driver)
        login.enter_login_username(uae_delivery)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل دلیوری دبی شد. ")
        delivery.enter_my_task_delivery_manager()
        # sleep(.5)
        delivery.enter_delivery_manager_my_task_all()
        delivery.enter_delivery_my_task_deliver_to_customer()
        delivery.enter_delivery_manager_my_task_update()
        sleep(1)
        delivery.enter_delivery_manager_my_task_search(a)
        sleep(1)
        delivery.enter_delivery_manager_my_task_search_btn()
        # delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order()
        # delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_text( "توضیحات تاییدیه دریافت شده توسط راننده")
        # delivery.enter_delivery_my_task_deliver_to_customer_receive_goods_this_order_msg_holder()
        # print("تاییدیه دریافت شده توسط راننده انجام شد. ")
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
        print("تست با موفقیت به پایان رسید. ")
        print("############################################")

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
