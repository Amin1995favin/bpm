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


class Test_Admin_Menu13(unittest.TestCase):
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
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(21, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'کالای سفارش', 'شماره ترک', 'ویرایش شده', 'ترخیص توسط', 'هزینه های غیر رسمی (ریال)', 'هزینه حقوق و عوارض گمرکی (ریال)', 'هزینه صورتحساب انبار (ریال)', 'هزینه نمونه برداری آزمایشگاه (ریال)', 'هزینه تعیین ماهیت آزمایشگاه (ریال)', 'هزینه نمونه برداری انبارهای عمومی (ریال)', 'سایر هزینه ها (ریال)', 'جمع هزینه ها (ریال)', 'زمان ایجاد هزینه صدور قبض', 'شماره بچ', 'صاحب پیش فاکتور'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ایجادکننده', 'زمان ایجاد', 'واحد عرض قبلی', 'نرخ واحد عرض جدید', 'نوع پیش فاکتور', 'شناسه آرین پیش فاکتور قبلی', 'تاییدیه اطلاع'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',  'وضعیت', 'مبلغ', 'سفارش', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',  'کاربر حذف شونده', 'کاربر نهایی', 'زمان ایجاد', 'ایجادکننده', 'عملیات'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'توضیحات مدیر مشتری برای مالی', 'توضیحات', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز', 'مبلغ پیش فاکتور', 'تاریخ ایجاد سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(5, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',  'سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'اطلاعات پیش فاکتور',  'تاریخچه تغییرات', 'بررسی'])
        admin.my_tasks_check("//*[@id='task-collapse-7']/div[1]/div/div/div[2]/a[10]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'مبلغ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت',  'حساب', 'زمان پرداخت', 'خروج از کارتابل'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
