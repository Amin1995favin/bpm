from selenium import webdriver
from time import sleep
from Locators import *
from Pages.Clearance.My_Tasks import My_Tasks
from Pages.Customer_Manager.Menu import Menu
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
import unittest
from selenium.webdriver.chrome.service import Service

from Pages.MongoDB.Mongo import Mongodb

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Clearance_Check_Order(unittest.TestCase):
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
        sleep(1)
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
        sleep(2)
        orders_create.enter_create_order_product_check_passed()
        print("############################################")

    ################### orders_create_products_check_price_unit ###################

    def test04_orders_create_products_check_price_unit(self):
        self.driver.implicitly_wait(10)
        orders_create = Orders_Create(driver=self.driver)
        orders_create.enter_orders_create_check_sender_city_btn2("Shenzhen - China")
        sleep(0.7)
        orders_create.enter_orders_create_sender_person("ملیکا کابلی")
        sleep(1)
        orders_create.enter_orders_create_check_receiver_city_btn2("tehran")
        sleep(0.7)
        orders_create.enter_orders_create_receiver_person("ملیکا کابلی")
        orders_create.enter_orders_create_information_factor_rasmi_transport()
        orders_create.enter_orders_create_information_factor_rasmi_transport_option()
        orders_create.enter_orders_create_information_factor_rasmi_clearance()
        orders_create.enter_orders_create_information_factor_rasmi_clearance_option()
        orders_create.enter_orders_create_information_factor_rasmi()
        orders_create.enter_orders_create_information_factor_rasmi_option()
        orders_create.enter_orders_create_information_approve()
        # sleep(1)
        # orders_create.enter_create_order_product_check_all_data2()
        # ________________________________________________________________
        orders_create.enter_product_final_order_confirmation()
        orders_create.enter_product_check_color_checking_the_order()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_product_details_of_this_order_are_approved()
        sleep(1)
        print("############################################")

    ################### Login_admin ###################

    def test05_login_admin(self):
        a = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a[1]/span").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        menu = Menu(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        login.enter_login_username(account_clearance1)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل ترخیص شد")
        print("############################################")

    ################### check_orders ###################

    # def test06_check_orders(self):
        sleep(1)
        orders_create.enter_click_orders()
        sleep(1)
        menu.enter_customer_manager_orders_check_create_order()
        menu.enter_customer_manager_orders_list_all_orders()
        menu.enter_customer_manager_orders_draft()
        menu.enter_customer_manager_orders_pre_order()
        menu.enter_customer_manager_orders_pending_approval()
        menu.enter_customer_manager_orders_canceled()
        menu.enter_customer_manager_orders_suspended()
        menu.enter_customer_manager_orders_doing_open()
        menu.enter_customer_manager_orders_picked_up()
        menu.enter_customer_manager_orders_delivered()
        # menu.enter_customer_manager_orders_delivered_settled()
        orders_create.enter_delivery_manager_click_orders_check_len()
        print("############################################")
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id_tn(a)

    ################### orders_create_products ###################

    def test06_orders_create_products(self):
        a = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a[1]/span").text
        # self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a[1]/span").click()
        self.driver.implicitly_wait(10)
        my_tasks = My_Tasks(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        orders_create.enter_check_clearance_manager_orders_doing_open()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_clearance_manager_checking_the_order()
        self.driver.back()
        orders_create.enter_click_checking_the_order()
        orders_create.enter_clearance_manager_check_box_chat()
        self.driver.back()
        orders_create.enter_click_box_barcode()
        orders_create.enter_clearance_manager_check_box_order_obligation()
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[1]/div[2]/table/thead/tr", 6, ['ردیف', 'عنوان فایل', 'فایل', 'تایید شده', 'زمان ایجاد', 'ایجادکننده'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[2]/div/div[2]/div/table/thead/tr", 7, ['ردیف', 'نام کالا', 'تصویر', 'فایل Proforma Invoice', 'فایل Packing List', 'سایر فایل های پیوست', 'سایر فایل های پیوست'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/div/table/thead/tr", 5, ['ردیف', 'متن', 'فایل پیوست', 'کاربر', 'زمان'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[4]/div/div[2]/div/table/thead/tr", 5, ['ردیف', 'فایل پیوست', 'کاربر', 'زمان', 'دریافت کننده'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[5]/div/div[2]/div/table/thead/tr", 5, ['ردیف', 'ثبت مدارک ترخیصیه', 'تصویر کارت بازرگانی', 'زمان ایجاد', 'ایجادکننده'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[6]/div/div[2]/div/table/thead/tr", 5, ['ردیف', 'فایل پیوست', 'کاربر', 'زمان', 'دریافت کننده'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[7]/div/div[2]/div/table/thead/tr", 5, ['ردیف', 'ثبت مدارک ترخیصیه', 'تصویر کارت بازرگانی', 'ایجادکننده', 'زمان ایجاد'])
        self.driver.back()
        orders_create.enter_click_box_order_obligation()
        orders_create.enter_delivery_manager_check_box_transporter_inquery()
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[2]/div//table/thead/tr", 5, ['ردیف', 'معتبر است؟', 'وضعیت', 'واحد و نرخ هر کیلو', 'کاربر ایجاد کننده'])
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[3]//table[@class='table table-striped']/tbody/tr", 4, ['ردیف', 'نام کالا', 'مشخصات وزن (KG)', 'وضعیت کالا'])
        self.driver.back()
        orders_create.enter_admin_click_box_transporter_inquery()
        my_tasks.enter_clearance_my_tasks_need_to_issue3()
        orders_create.enter_check_box_clearance_inquery()
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[2]/div//table/thead/tr", 14, ['ردیف', 'معتبر است؟', 'ترخیص کار', 'نوع ترخیص', 'قیمت', 'قیمت هر کیلو', 'واحد', 'وزن جرمی', 'قیمت نهایی', 'پیش فاکتور رسمی؟', 'یادداشت', 'زمان ایجاد', 'ایجادکننده', 'صادر شده بعد از بارگیری'])
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[3]/div//table/thead/tr", 8, ['ردیف', 'شماره پیش فاکتور', 'عنوان', 'قیمت اعلامی', 'قیمت نهایی', 'تسعیر ارز', 'عملیات', 'کاربر ایجاد کننده'])
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[5]/div//table/thead/tr", 7, ['ردیف', 'تاریخ تحویل قبض', 'ایجادکننده', 'زمان ایجاد', 'نماینده', 'ترک نامبر', 'شماره ترک فرعی'])
        self.driver.back()
        self.driver.back()
        orders_create.enter_click_box_clearance_inquery()
        orders_create.enter_check_box_other_service_inquery()
        orders_create.check_table("//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr", 10, ['ردیف', 'معتبر است؟', 'عنوان', 'نوع پیش فاکتور', 'قیمت', 'واحد', 'توضیحات خدمت', 'پیش فاکتور رسمی؟', 'زمان ایجاد', 'ایجادکننده'])
        self.driver.back()
        orders_create.enter_admin_click_box_other_service_inquery()
        scrolled1 = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[9]/div[2]/a[1]")
        sleep(1)
        scrolled1.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_send_invoice_not_sent_to_the_customer()
        print("فاکتور حمل به مشتری ارسال شد. ")
        self.driver.refresh()
        sleep(1)
        scrolled2 = self.driver.find_element('xpath', "//table/tbody/tr[1]/td[9]/div[3]/a[1]")
        sleep(1)
        scrolled2.location_once_scrolled_into_view
        tasks_list.enter_customer_manager_my_tasks_conformation_by_customer_approval()
        print("فاکتور حمل توسط مشتری تایید شد. ")
        orders_create.enter_delivery_manager_check_box_invoices()
        self.driver.back()
        orders_create.enter_admin_click_box_invoices()
        orders_create.enter_clearance_manager_check_box_op()
        orders_create.check_table("//*[@id='fatherdiv']/div[2]/div//table/thead/tr", 3, ['ردیف', 'شماره ترک', 'عملیات'])
        self.driver.back()
        orders_create.enter_admin_click_box_payment()
        orders_create.enter_clearance_manager_check_box_logs()

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Clearance_Check_Order, 'Clearance_Check_Order')
