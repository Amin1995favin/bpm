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

from Pages.MongoDB.Mongo import Mongodb

service = Service()
options = webdriver.ChromeOptions()
# options.add_argument("--headless")

driver = webdriver.Chrome(service=service, options=options)


class Test_Admin_Menu10(unittest.TestCase):
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
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[15]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[16]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی', 'کدملی', 'موبایل1', 'موبایل2', 'تلفن ثابت 1', 'وضعیت', 'توضیحات عدم تایید'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[17]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شخص ارسال کننده', 'خدمات موردنیاز', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[18]")
        sleep(2)
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'مقصد', 'توضیحات علت برگشت', 'تاییدیه اصلاح اطلاعات'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[19]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[20]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', '', 'سفارش', 'جزئیات', 'وزن سفارش (KG)', 'شهر مبدا', 'کالاهای ریپک', 'تایید درخواست ریپک'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[21]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', 'لیست', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'سفارش', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[22]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور خرید'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[23]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی', 'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده', 'تعداد سفارشات', 'کارکرد مالی'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[24]")
        sleep(2)
        my_tasks.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'دفعات بارگیری سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[25]")
        sleep(2)
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'عنوان', 'قیمت اعلامی', 'پرداخت شده (در واحد)'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[26]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'توضیحات مالی', 'توضیحات مدیر مشتری برای دلیوری', 'توضیحات مدیر مشتری برای مالی', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[27]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ایراد تسویه', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[28]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'عملیات', 'نام و نام خانوادگی', 'دوره تجدید سفارش', 'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده', 'تعداد سفارشات', 'کارکرد مالی'])



    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()


Mongodb.run_tests_and_insert_into_mongodb(Test_Admin_Menu10, 'Admin_Menu10')

