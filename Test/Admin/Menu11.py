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


class Test_Admin_Menu11(unittest.TestCase):
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
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'شهر مبدا', 'شهر مقصد', 'سفارش', 'کالای سفارش', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(14, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'شهر مبدا', 'درخواست های ریپک', 'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        sleep(1)
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد استعلام ترخیص', 'سفارش', 'کالای سفارش',  'زمان ایجاد', 'نوع حمل', 'وزن سفارش (KG)', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع پیش فاکتور حمل'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'شماره پیگیری', 'زمان ورود وظیفه به این کارتابل', 'تاریخ قبض شدن', 'تاریخ تحویل قبض', 'ترخیص کار', 'آخرین آپدیت ترخیص',  'ذخیره اطلاعات ترخیص', 'تاریخچه تغییرات'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'شناسه', 'زمان ورود وظیفه به این کارتابل', 'مبدا', 'مقصد', 'وزن قابل پرداخت', 'فایل های بچ',  'هزینه', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', 'شماره بسته', 'زمان ورود وظیفه به این کارتابل', 'موقعیت', 'تاریخ تخمینی رسیدن بار', 'وزن جرمی', 'تعداد سفارش',  'تعداد کالا سفارش', 'وضعیت تایید', 'خروج از کارتابل'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[8]")
        # sleep(2)
        # my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'شماره ترک فرعی', 'ثبت اطلاعات تحویل قبض', 'تحویل قبض'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز',  'بروزرسانی'])
        sleep(2)
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[10]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'وزن سفارش (KG)', 'شماره بچ',  'ثبت اطلاعات تحویل قبض'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش',  'جمع وزن جرمی (kg)', 'ارزش کل', 'واحد ارزش', 'توضیحات', 'نوع پیش فاکتور ترخیص', 'قیمت پایه ترخیص به ریال'])
        admin.my_tasks_check("//*[@id='task-collapse-1']/div[1]/div/div/div[2]/a[13]")
        my_tasks.my_tasks_check_table(15, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره ترک فرعی',  'وزن سفارش (KG)', 'دریافت کننده', 'نوع ترخیص', 'فایل های قبضی', 'تصویر کارت بازرگانی', 'شناسه ملی', 'نام صاحب شناسه ملی', 'نام انگلیسی صاحب شناسه ملی', 'توضیحات'])

















    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
