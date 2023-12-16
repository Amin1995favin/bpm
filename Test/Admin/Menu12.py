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


class Test_Admin_Menu12(unittest.TestCase):
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
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(14, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'شهر مبدا', 'درخواست های ریپک', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ', 'تاریخ تحویل'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[5]")
        sleep(1)
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'شماره ترک فرعی', 'ثبت اطلاعات تحویل قبض', 'تحویل قبض'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[2]/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز',  'بروزرسانی'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
