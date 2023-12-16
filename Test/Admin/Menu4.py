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


class Test_Admin_Menu4(unittest.TestCase):
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

    def test02_admin_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بازاریاب', 'دریافت کننده', 'ارسال کننده', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'ایجادکننده'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بازاریاب', 'بازیاب بازاریابی', 'کارشناس فروش', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نوع تخفیف', 'سفارش', 'مبلغ درخواستی', 'واحد', 'علت تخفیف', 'توضیحات', 'کاربر ثبت کننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره بچ', 'هزینه های ثبت نشده', 'وزن سفارش (KG)', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(12, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نوع تخفیف', 'سفارش', 'مبلغ درخواستی', 'واحد', 'علت تخفیف', 'توضیحات', 'کاربر ثبت کننده', 'مدیر مشتری'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'دفعات بارگیری سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کاربر', 'مبلغ', 'واحد', 'توضیحات', 'زمان تغییرات'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'عملیات', 'توضیحات نوع کالا', 'سفارش', 'وزن سفارش (KG)', 'تاییدیه حمل', 'دسته بندی کلی کالا', 'دسته بندی جزئی کالا'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کاربر حذف شونده', 'کاربر نهایی', 'زمان ایجاد', 'ایجادکننده'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[10]")
        my_tasks.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'اطلاعات سفارش', 'واحد و نرخ هر کیلو'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'دریافت کننده', 'ارسال کننده', 'وزن سفارش (KG)', 'کالای سفارش', 'خدمات موردنیاز'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[13]")
        # my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ترخیص', 'خدمات موردنیاز', 'مقصد سفارش', 'توضیحات درخواست', 'کالاهای سفارش'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[14]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'کد مشخصه', 'موقعیت', 'ترک فرعی', 'جمع وزن جرمی(kg)', 'ارزش', 'توضیحات'])
        admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[15]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص دریافت کننده', 'شخص ارسال کننده', 'نوع حمل', 'وزن سفارش (KG)', 'نوع پیش فاکتور حمل'])
        # admin.my_tasks_check("//*[@id='task-collapse-5']/div[1]/div/div/div[2]/a[16]")
        # my_tasks.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شهر مبدا', 'شهر مقصد'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
