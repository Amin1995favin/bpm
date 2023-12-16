from selenium import webdriver
from time import sleep
from Locators import *
from Pages.Customer_Manager.Tasks_List import Tasks_list

from Pages.Export.Menu import Export_My_Tasks
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Export_Menu_Others2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_export ###################

    def test01_export(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_export)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت شد. ")
        print("############################################")

    ################### export_check_my_tasks ###################

    def test02_export_check_my_tasks_others(self):
        tasks_list = Export_My_Tasks(driver=self.driver)
        tasks = Tasks_list(driver=self.driver)
        tasks.enter_customer_manager_my_tasks()
        tasks_list.enter_export_my_tasks_warehouse()
        tasks_list.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[1]")
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص ارسال کننده', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        tasks_list.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[2]")
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        # tasks_list.my_tasks_check("//*[@id='nav-category-3']/div/div/div/div[2]/a[3]")
        # tasks_list.my_tasks_check_table(5, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'فایل های قبضی', 'آماده تحویل به مشتری'])
        tasks_list.enter_export_my_tasks_financial()
        # tasks_list.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a[1]")
        # tasks_list.my_tasks_check_table(9, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        tasks_list.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a[2]")
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش',  'توضیحات مدیر مشتری برای مالی', 'توضیحات', 'مشخصات وزن (KG)', 'خدمات موردنیاز'])
        tasks_list.my_tasks_check("//*[@id='nav-category-7']/div/div/div/div[2]/a[3]")
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        tasks_list.enter_export_my_tasks_delivery()
        tasks_list.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a[1]")
        tasks_list.my_tasks_check_table(11, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'نوع ترخیص', 'شماره بچ', 'فایل های سفارش', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])
        tasks_list.my_tasks_check("//*[@id='nav-category-8']/div/div/div/div[2]/a[2]")
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'هماهنگی های انجام شده', 'نوع ترخیص', 'فایل های سفارش', 'علت بازگشت از آماده تحویل به مشتری'])
        tasks_list.enter_export_my_tasks_manager()
        tasks_list.my_tasks_check("//*[@id='nav-category-5']/div/div/div/div[2]/a[1]")
        tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کد مشخصه', 'موقعیت', 'ترک فرعی', 'جمع وزن جرمی(kg)', 'ارزش', 'توضیحات'])
        tasks_list.my_tasks_check("//*[@id='nav-category-5']/div/div/div/div[2]/a[2]")
        # tasks_list.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ترخیص', 'خدمات موردنیاز', 'مقصد سفارش', 'توضیحات درخواست', 'کالاهای سفارش'])
        tasks_list.my_tasks_check("//*[@id='nav-category-5']/div/div/div/div[2]/a[3]")
        tasks_list.my_tasks_check_table(7, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        tasks_list.my_tasks_check("//*[@id='nav-category-5']/div/div/div/div[2]/a[4]")
        tasks_list.my_tasks_check_table(10, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'نوع تخفیف', 'سفارش', 'مبلغ درخواستی', 'واحد', 'علت تخفیف', 'توضیحات', 'کاربر ثبت کننده', 'مدیر مشتری'])
        tasks_list.my_tasks_check("//*[@id='nav-category-5']/div/div/div/div[2]/a[5]")
        tasks_list.my_tasks_check_table(4, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'اطلاعات سفارش', 'واحد و نرخ هر کیلو'])
        tasks_list.my_tasks_check("//*[@id='nav-category-5']/div/div/div/div[2]/a[6]")
        tasks_list.my_tasks_check_table(6, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
