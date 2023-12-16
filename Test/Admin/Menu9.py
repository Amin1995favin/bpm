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


class Test_Admin_Menu9(unittest.TestCase):
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
        sleep(1)
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره پیش فاکتور', 'عنوان', 'قیمت اعلامی', 'نرخ تبدیل به ریال', 'ضریب مالیات', 'قیمت نهایی', 'کاربر ثبت کننده', 'زمان ثبت'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'پیش فاکتور به نام فرد', 'پیش فاکتور به نام شرکت'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'نوع حمل'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال', 'اعلام نقص مدرک'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[9]")
        sleep(1)
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مشخصات وزن (KG)', 'نوع ترخیص', 'خدمات موردنیاز', 'بروزرسانی', 'مقصد سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[10]")
        my_tasks.my_tasks_check_table(6, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[13]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بروزرسانی', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'تایید مدیریت'])
        admin.my_tasks_check("//*[@id='task-collapse-4']/div[2]/div/div/div[2]/a[14]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'کالای سفارش', 'علت لغو', 'حساب', 'وضعیت', 'زمان پرداخت', 'ایجادکننده', 'خروج از کارتابل'])


    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
