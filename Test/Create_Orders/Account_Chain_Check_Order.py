from selenium import webdriver
from time import sleep
from Locators import *
from Pages.Clearance.My_Tasks import My_Tasks
from Pages.Customer_Manager.Menu import Menu
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
from Pages.Customer_Manager.Orders_Create import Orders_Create
import unittest

from Pages.MongoDB.Mongo import Mongodb
from Pages.Warehouses.Menu import Warehouses_My_Tasks
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)

# driver = webdriver.Chrome(ChromeDriverManager().install())


class Test_Account_Chain_Check_Order(unittest.TestCase):
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

    ################### Login_account_chain ###################

    def test05_login_account_chain(self):
        a = self.driver.find_element('xpath', "//*[@id='main-content-wrapper']/section[1]/h1/a[1]/span").text
        print(a)
        self.driver.get(base_url)
        login = LoginPage(driver=self.driver)
        chain = Warehouses_My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        login.enter_login_username(account_chain)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر شعبه چین شد")
        print("############################################")

    ################### check_orders ###################

    # def test06_check_orders(self):
        sleep(1)
        chain.chain_click_orders()
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
        chain.enter_click_orders_check_len()
        print("############################################")
        orders_create.enter_click_orders_doing_open()
        orders_create.enter_click_orders_id_tn(a)

    ################### orders_create_products ###################

    def test06_orders_create_products(self):
        self.driver.implicitly_wait(10)
        my_tasks = My_Tasks(driver=self.driver)
        orders_create = Orders_Create(driver=self.driver)
        tasks_list = Tasks_list(driver=self.driver)
        orders_create.enter_check_account_chain_orders_doing_open()
        orders_create.enter_product_click_checking_the_order()
        orders_create.enter_account_chain_checking_the_order()
        orders_create.check_table("//*[@id='oplist100']/div[2]/div//table/thead/tr", 24, ['No.', 'ID', 'General category of goods', 'Detailed classification of goods', 'Product name', 'Unit number', 'Quantity', 'Unit Weight (kg)', 'Sum Weight (kg)', 'Chargeable weight', 'Unit Length (cm)', 'cbm', 'Volumetric weight', 'Number product per box', 'Unit value', 'Cargo Whole value', 'HSCODE', 'Part number', 'Purchase Link', 'Image', 'Proforma invoice file', 'Packing list file', 'Other attachments', 'Description'])
        orders_create.check_table("//*[@id='oplist1']/div[2]/div//table/thead/tr", 24, ['No.', 'ID', 'General category of goods', 'Detailed classification of goods', 'Product name', 'Unit number', 'Quantity', 'Unit Weight (kg)', 'Sum Weight (kg)', 'Chargeable weight', 'Unit Length (cm)', 'cbm', 'Volumetric weight', 'Number product per box', 'Unit value', 'Cargo Whole value', 'HSCODE', 'Part number', 'Purchase Link', 'Image', 'Proforma invoice file', 'Packing list file', 'Other attachments', 'Description'])
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div/div[5]/div/div/div[2]/div//table/thead/tr", 6, ['No.', 'Product name', 'Image', 'Proforma invoice file', 'Packing list file', 'Other attachments'])
        self.driver.back()
        orders_create.enter_click_checking_the_order()
        orders_create.enter_account_chain_check_box_chat()
        self.driver.back()
        orders_create.enter_click_box_barcode()
        self.driver.back()
        orders_create.enter_click_box_order_obligation()
        orders_create.enter_delivery_manager_check_box_order_obligation()
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[1]/div[2]/table/thead/tr", 6, ['No.', 'title', 'file', 'Accepted', 'Time created', 'Creator'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[2]/div/div[2]/div/table/thead/tr", 7, ['No.', 'Product name', 'Image', 'Proforma invoice file', 'Packing list file', 'Other attachments', 'History'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[3]/div/div[2]/div/table/thead/tr", 5, ['No.', 'Text', 'Attached file', 'User', 'Time'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[4]/div/div[2]/div/table/thead/tr", 5, ['No.', 'Attached file', 'User', 'Time', 'receiver'])
        # orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[5]/div/div[2]/div/table/thead/tr", 5, ['No.', 'Registration of clearance documents', 'Business card image', 'Creator', 'Creation time'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[6]/div/div[2]/div/table/thead/tr", 5, ['No.', 'Attached file', 'User', 'Time', 'receiver'])
        orders_create.check_table("/html/body/div[1]/div[1]/section[2]/div[7]/div/div[2]/div/table/thead/tr", 5, ['No.', 'Registration of clearance documents', 'Business card image', 'Creator', 'Creation time'])
        self.driver.back()
        orders_create.enter_admin_click_box_transporter_inquery()
        orders_create.enter_customer_manager_check_box_transporter_inquery()
        # orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[1]/div//table/thead/tr", 16, ['No.', 'Is it valid?', 'Transportation type', 'Transporter', 'Inquiry type', 'Payable weight', 'Price approved', 'Price', 'Price per kilo', 'the unit', 'Official invoice?', 'Delivery time', 'Description', 'Time created', 'Creator', 'Issued after receipt'])
        orders_create.check_table("//*[@id='discountperkilo']//table/thead/tr", 5, ['No.', 'Is it valid?', 'Condition', 'واحد و نرخ هر کیلو', 'کاربر ایجاد کننده'])
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[4]//table[@class='table table-striped']/tbody/tr", 4, ['No.', 'Product name', 'Weight Specification (KG)', ' Commodity status'])
        self.driver.back()
        orders_create.enter_click_box_clearance_inquery()
        orders_create.enter_customer_manager_check_box_clearance_inquery()
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div/div/div/div[1]/div/div[2]/div//table/thead/tr", 7, ['No.', 'Receipt delivery date', 'Creator', 'Creation time', 'Agent', 'leave number', 'Sub track number'])
        self.driver.back()
        orders_create.enter_admin_click_box_other_service_inquery()
        orders_create.enter_check_box_other_service_inquery()
        orders_create.check_table("//table[@class=' table  table-striped  table-hover  sort-table ']/thead/tr", 10, ['No.', 'Is it valid?', 'Title', 'Other pre-factor type', 'Price', 'Unit', 'Service description', 'Official invoice?', 'Time created', 'Creator'])
        self.driver.back()
        orders_create.enter_admin_click_box_invoices()
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
        orders_create.enter_account_chain_check_box_invoices()
        self.driver.back()
        orders_create.enter_admin_click_box_payment()
        orders_create.enter_customer_manager_check_box_payment()
        orders_create.check_table("//*[@id='payment_tn']/div//table/thead/tr", 9, ['No.', 'Condition', 'Amount', 'Pre-assigned to factors', 'Account', 'Payment tracking number', 'Description', 'Confirmation description', 'Creator'])
        self.driver.back()
        orders_create.enter_admin_click_order_loaded_goods()
        orders_create.enter_account_chain_check_order_loaded_goods()
        self.driver.back()
        orders_create.enter_admin_click_box_op()
        orders_create.enter_account_chain_check_box_op()
        self.driver.back()
        orders_create.enter_admin_click_box_china_transaction()
        orders_create.enter_check_box_china_transaction()
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[1]//table/thead/tr", 14, ['No.', 'Transaction type', 'Title', 'Price', 'The final price', 'the unit', 'Rate of conversion to Rials', 'price in rials', 'Description', 'attached file', 'Is it valid?', 'done', 'Does it have a pre-invoice?', 'Creator	'])
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[1]/div/div[2]//table/thead/tr", 7, ['No.', 'کاربر', 'وضعیت درخواست', 'مبلغ', 'واحد', 'توضیحات', 'Time for change'])
        self.driver.back()
        orders_create.enter_admin_click_box_invoices_discount()
        orders_create.enter_check_box_invoices_discount()
        orders_create.check_table("//*[@id='main-content-wrapper']/section[2]/div[1]/div//table/thead/tr", 10, ['No.', 'وضعیت تایید', 'شناسه پیش فاکتور', 'قیمت', 'واحد', 'علت تخفیف', 'توضیحات', 'کاربر ثبت کننده', 'کاربر تایید کننده / رد کننده', 'Non-authenticating user'])
        self.driver.back()
        orders_create.enter_admin_click_box_logs()
        orders_create.enter_account_chain_check_box_logs()
        self.driver.back()
        orders_create.enter_admin_click_box_arian()
        orders_create.enter_account_chain_check_box_track_order()
        orders_create.check_table("//*[@id='pageHolder']/div[1]/div//table/thead/tr", 9, ['No.', 'Status', 'Time', 'Description', 'Creator', 'Time created', 'Updated by', 'Time updated',' '])
        orders_create.check_table("//*[@id='pageHolder']/div[2]/div/div[2]/div//table/thead/tr", 7, ['No.', 'PSP tracking number', 'Carrier company', 'Tracking carrier number', 'Bill of lading image', 'file', 'Description'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Account_Chain_Check_Order, 'Account_Chain_Check_Order')
