from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Clearance.Menu import My_Tasks
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


class Test_Admin_Menu1(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_admin ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_admin02)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت شد. ")
        print("############################################")

    ################## admin_check_menu ###################

    def test02_admin_check_menu(self):
        admin = Admin_My_Tasks(driver=self.driver)
        menu = Menu(driver=self.driver)
        admin.enter_admin_menu_check_tag()
        admin.enter_admin_menu_check_tag_dashboard()
        admin.enter_admin_menu_check_name()
        menu.enter_customer_manager_menu_check_search()
        admin.admin_dashboard()
        admin.admin_my_task()
        admin.admin_inbox()
        admin.admin_train()
        admin.admin_report()
        admin.admin_orders()
        admin.admin_warehouses()
        admin.admin_fast_bill_scan()
        admin.admin_accept_order_op_by_scan()
        admin.admin_batches()
        admin.admin_persons()
        # admin.admin_companies()
        admin.admin_new_relabel()
        admin.admin_delivery_info_search()
        admin.admin_shipping_cost()
        admin.admin_exchangerates()
        # admin.admin_exchange_rate_profits()
        admin.admin_last_payments()
        admin.admin_last_yuan_payment()
        admin.admin_china_expenses()
        admin.admin_china_expenses_costs()
        admin.admin_crypto_gateway_recovery()
        # admin.admin_expert_chat()
        admin.admin_phone_marketer_calls()
        admin.admin_iran_china_offices()
        admin.admin_customer_messages()
        admin.admin_festivals()
        admin.admin_excel_export_files()
        admin.admin_path_menu()
        admin.admin_pkgs()
        admin.admin_task()
        admin.admin_settings()
        admin.admin_customer_expert_messages()
        admin.admin_profile()
        admin.admin_change_pass()
        admin.admin_exit()
        admin.enter_admin_menu_check_tag_dashboard()
        print("تمام موارد منوی مدیر به درستی نمایش داده شد.")
        print("_________________________________________________________")

    ################### admin_warehouses_check_my_tasks ###################

    def test03_admin_warehouses_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        admin.len_admin()
        sleep(1)
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'کالاهای سفارش', 'توضیحات بسته بندی', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص ارسال کننده', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کل مبلغ بدهی بابت این سفارش (ریال)', 'مبلغ مازاد بر سفارش', 'توضیحات دلیوری', 'تاریخ تحویل', 'نام تحویل گیرنده', 'شماره تماس تحویل گیرنده', 'آدرس محل تحویل', 'نحوه ی پرداخت مالی سفارش جهت تحویل'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'فایل های قبضی', 'آماده تحویل به مشتری', 'تاییدیه پرینت مدارک و تحویل به دلیوری'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', 'شماره ترک', 'زمان ورود وظیفه به این کارتابل', 'مدیر مشتری', 'تعداد کالا', 'ارزش ترک (دلار)', 'PL', 'PI', 'شماره بچ', 'چاپ', 'خروج از کارتابل', 'ویرایش'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', 'شماره ترک', 'زمان ورود وظیفه به این کارتابل', 'مدیر مشتری', 'تعداد کالا', 'ارزش ترک (دلار)', 'PL', 'PI', 'شماره بچ', 'چاپ', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'نوع ترخیص', 'مقصد', 'بچ های سفارش', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[1]/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'وزن سفارش (KG)'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Admin_Menu1, 'Admin_Menu1')
