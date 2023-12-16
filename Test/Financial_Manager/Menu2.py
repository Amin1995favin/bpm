from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Financial_Manager.Menu import Financial_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)



class Test_Financial_Menu2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_financial_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(financial_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مالی شد. ")
        print("############################################")

    ################### financial_check_my_tasks ###################

    def test02_financial_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        financial = Financial_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        financial.arian_register_cryp_to_payments()
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'مبلغ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت',  'حساب', 'زمان پرداخت', 'خروج از کارتابل'])
        # financial.order_owner_migration_to_arian()
        # my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی', 'کدملی', 'موبایل1', 'موبایل2', 'تلفن ثابت 1', 'عملیات'])
        financial.my_tasks_need_official_invoice()
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'توضیحات مدیر مشتری برای مالی', 'توضیحات', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        # financial.submit_in_financial_system()
        # my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز', 'مبلغ پیش فاکتور', 'تاریخ ایجاد سفارش'])
        # financial.factors_chang_after_insert_arian()
        # my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'پیش فاکتور', 'نوع فاکتور', 'نرخ قدیم فاکتور', 'نرخ جدیدفاکتور', 'تاییدیه اطلاع', 'نوع'])
        financial.china_transaction_log()
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'وضعیت', 'زمان ورود وظیفه به این کارتابل', 'دلیل', 'عنوان', 'قیمت', 'واحد', 'ایجادکننده', ' '])
        financial.settled_no_payment()
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'پیش فاکتور',  'پرداخت شده (در واحد)', 'کاربر ثبت کننده', 'تایید مالی'])
        financial.check_commission_payment_request()
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'مبلغ پورسانت (ریال)', 'سفارش های مرتبط', 'ایجادکننده', 'زمان ایجاد'])
        financial.arian_register_foreign_payments()
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', 'وضعیت', 'زمان ورود وظیفه به این کارتابل', 'مبلغ', 'حساب', 'توضیحات', 'زمان پرداخت', 'ایجادکننده', 'شماره حساب/کارت پرداخت کننده', 'نام صاحب حساب پرداخت کننده', 'علت عدم انتخاب موارد مشابه'])
        financial.auto_wallet_refund()
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        # financial.new_of_invoice_after_print_delivery()
        # my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])






    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
