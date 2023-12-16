from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)


class Test_Admin_Menu14(unittest.TestCase):
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

    ################### admin_check_my_tasks ###################

    def test02_admin_customer_manager_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی', 'کدملی', 'موبایل1', 'موبایل2', 'تلفن ثابت 1', 'عملیات'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'توضیحات مدیر مشتری برای مالی', 'توضیحات', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[13]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز', 'مبلغ پیش فاکتور', 'تاریخ ایجاد سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[14]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'پیش فاکتور', 'نوع فاکتور', 'نرخ قدیم فاکتور', 'نرخ جدیدفاکتور', 'تاییدیه اطلاع', 'نوع'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[15]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'وضعیت', 'زمان ورود وظیفه به این کارتابل', 'دلیل', 'عنوان', 'قیمت', 'واحد', 'ایجادکننده', ' '])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[16]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'پیش فاکتور',  'پرداخت شده (در واحد)', 'کاربر ثبت کننده', 'تایید مالی'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[17]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'مبلغ پورسانت (ریال)', 'سفارش های مرتبط', 'ایجادکننده', 'زمان ایجاد'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[18]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', 'وضعیت', 'زمان ورود وظیفه به این کارتابل', 'مبلغ', 'حساب', 'توضیحات', 'زمان پرداخت', 'ایجادکننده', 'شماره حساب/کارت پرداخت کننده', 'نام صاحب حساب پرداخت کننده', 'علت عدم انتخاب موارد مشابه'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[19]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[20]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[21]")
        my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
