from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Uae.Menu import Uae
from Pages.Admin.Menu import Admin_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Uae_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_admin ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_uae)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر شعبه امارات شد. ")
        print("############################################")

    ################### admin_dubai_check_my_tasks_others ###################

    def test02_admin_dubai_check_my_tasks_others(self):
        my_tasks = My_Tasks(driver=self.driver)
        uae = Uae(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        uae.len_dubai_my_tasks()
        uae.click_financial()
        admin.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        uae.click_delivery()
        admin.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره بچ', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])
        admin.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'عملیات', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'هماهنگی های انجام شده', 'نوع ترخیص', 'فایل های سفارش', 'علت بازگشت از آماده تحویل به مشتری'])
        uae.click_customer_manager()
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'ارسال کننده', 'دریافت کننده', 'شهر مبدا', 'کد پستی', 'آدرس'])
        admin.my_tasks_check("//*[@id='nav-category-4']/div/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ارسال کننده', 'دریافت کننده', 'تاریخ و زمان آمادگی فرستنده جهت پیک آپ', 'توضیحات تاریخ و زمان آمادگی فرستنده'])
        uae.click_customer_export()
        admin.my_tasks_check("//*[@id='nav-category-2']/div/div/div/div[2]/a")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'ارزش کل', 'توضیحات', 'نوع پیش فاکتور خرید'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
