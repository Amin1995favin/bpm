from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep
from Locators import *

from Pages.Clearance.Menu import My_Tasks
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Customer_Manager.Menu import Menu
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service

from Pages.MongoDB.Mongo import Mongodb

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)


class Test_Clearance_Menu(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)
        cls.tests_texts = []


    ################### Login_clearance ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        my_tasks = My_Tasks(driver=self.driver)
        login.enter_login_username(account_clearance)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر واحد استعلام ترخیص شد")
        print("############################################")

    ################### clearance_check_menu ###################

    def test02_clearance_check_menu(self):
        my_tasks = My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        my_tasks.enter_clearance_menu_check_tag()
        my_tasks.enter_clearance_menu_check_tag_dashboard()
        my_tasks.enter_clearance_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        menu.enter_customer_manager_menu_check_dashboard()
        menu.enter_customer_manager_menu_check_my_tasks()
        menu.enter_customer_manager_menu_check_inbox()
        menu.enter_customer_manager_menu_check_information_and_training()
        menu.enter_customer_manager_menu_check_management_reports()
        menu.enter_customer_manager_menu_check_orders()
        my_tasks.enter_clearance_warehouses()
        my_tasks.enter_clearance_warehouses_fast_bill_scan()
        my_tasks.enter_clearance_warehouses_accept_order_op_by_scan()
        my_tasks.enter_clearance_batches()
        my_tasks.enter_clearance_menu_shipping_rate()
        my_tasks.enter_clearance_menu_check_exchange_rates()
        my_tasks.enter_clearance_menu_check_list_excel_output()
        my_tasks.enter_clearance_menu_settings()
        my_tasks.enter_clearance_menu_check_user_profile()
        my_tasks.enter_clearance_menu_check_change_password()
        my_tasks.enter_clearance_menu_check_exit()
        print("تمام موارد منوی مدیر ترخیص به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### clearance_check_my_tasks ###################

    def test03_clearance_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        my_tasks.len_clearance()
        my_tasks.need_clearance_inquiry()
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        # my_tasks.cleared_orders()
        # my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        my_tasks.need_final_clearance()
        my_tasks.my_tasks_check_table(14, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'شهر مبدا', 'درخواست های ریپک', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        my_tasks.auto_other_clearance()
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'سفارش', 'کالای سفارش',  'زمان ایجاد', 'نوع حمل', 'وزن سفارش (KG)', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع پیش فاکتور حمل'])
        my_tasks.clearance_update()
        my_tasks.my_tasks_check_table(9, ['ردیف', 'شماره پیگیری', 'زمان ورود وظیفه به این کارتابل', 'تاریخ قبض شدن', 'تاریخ تحویل قبض', 'ترخیص کار', 'آخرین آپدیت ترخیص',  'ذخیره اطلاعات ترخیص', 'تاریخچه تغییرات'])
        my_tasks.batch_files_in_formation()
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'شناسه', 'زمان ورود وظیفه به این کارتابل', 'مبدا', 'مقصد', 'وزن قابل پرداخت', 'فایل های بچ',  'هزینه', 'خروج از کارتابل'])
        my_tasks.notification_closure_batch()
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', 'شماره بسته', 'زمان ورود وظیفه به این کارتابل', 'موقعیت', 'تاریخ تخمینی رسیدن بار', 'وزن جرمی', 'تعداد سفارش',  'تعداد کالا سفارش', 'وضعیت تایید', 'خروج از کارتابل'])
        # my_tasks.auto_billed_order()
        # my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'شماره ترک فرعی', 'ثبت اطلاعات تحویل قبض', 'تحویل قبض'])
        my_tasks.pickup_by_customs()
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز',  'بروزرسانی'])
        my_tasks.new_auto_billed_order()
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'ثبت اطلاعات تحویل قبض'])
        my_tasks.auto_need_clearance_invoice_sea()
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        my_tasks.auto_need_clearance_invoice_sea_finaly()
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Clearance_Menu, 'Clearance_Menu')

