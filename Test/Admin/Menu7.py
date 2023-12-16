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


class Test_Admin_Menu7(unittest.TestCase):
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
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', '', 'سفارش', 'جزئیات', 'وزن سفارش (KG)', 'شهر مبدا', 'کالاهای ریپک', 'تایید درخواست ریپک'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', 'لیست', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'سفارش', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[13]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور خرید'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[14]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شماره ترک فرعی', 'مبدا', 'مقصد', 'وزن سفارش (KG)', 'اطلاع رسانی به مشتری', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[15]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شهر ارسال کننده', 'شهر دریافت کننده', 'نام شرکت', 'شماره پیگیری شرکت حمل کننده', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[16]")
        my_tasks.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[17]")
        my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مبلغ', 'توضیحات'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[18]")
        my_tasks.my_tasks_check_table(15, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شخص ارسال کننده', 'شرکت ارسال کننده', 'تلفن تماس شخص فرستنده', 'تاریخ و زمان آمادگی فرستنده جهت پیک آپ', 'توضیحات تاریخ و زمان آمادگی فرستنده', 'شماره ترک سفارش در شرکت حمل کننده', 'نام شرکت حمل کننده', 'فایل پیوست', 'لیبل 1', 'لیبل 2', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[19]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی', 'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده', 'تعداد سفارشات', 'کارکرد مالی'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[20]")
        sleep(1)
        my_tasks.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'دفعات بارگیری سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[21]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ایراد تسویه', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[22]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'تاییدیه درخواست های خرید', 'سفارش', 'مبدا', 'مقصد', 'خدمت', 'لیست کالاها', 'اطلاعات درخواست خرید', 'عملیات', 'ایجادکننده'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[23]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'تاییدیه درخواست های خرید', 'سفارش', 'مبدا', 'مقصد', 'خدمت', 'لیست کالاها', 'اطلاعات درخواست خرید', 'عملیات', 'ایجادکننده'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[1]/div/div/div[2]/a[24]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'تایید مدیریت'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
