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


class Test_Admin_Menu16(unittest.TestCase):
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
        admin.my_tasks_check("//*[@id='task-collapse-8']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'نوع ترخیص', 'شماره بچ', 'فایل های سفارش', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])
        admin.my_tasks_check("//*[@id='task-collapse-8']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'عملیات', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'هماهنگی های انجام شده', 'نوع ترخیص', 'فایل های سفارش', 'علت بازگشت از آماده تحویل به مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-8']/div[1]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره ترک فرعی', 'فایل های قبضی', 'آماده تحویل به مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-8']/div[1]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'زمان ورود به انبار', 'سفارش', 'شماره ترک', 'نوع ترخیص', 'بچ های سفارش', 'تعداد پارت'])
        admin.my_tasks_check("//*[@id='task-collapse-8']/div[2]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'نوع ترخیص', 'شماره بچ', 'فایل های سفارش', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])
        admin.my_tasks_check("//*[@id='task-collapse-8']/div[2]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'عملیات', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'هماهنگی های انجام شده', 'نوع ترخیص', 'فایل های سفارش', 'علت بازگشت از آماده تحویل به مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-11']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'علت لغو', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        admin.my_tasks_check("//*[@id='task-collapse-11']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'آخرین تماس', 'صاحب سفارش', 'سفارش های کاربر', 'عملیات'])
        admin.my_tasks_check("//*[@id='task-collapse-2']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        admin.my_tasks_check("//*[@id='task-collapse-2']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
