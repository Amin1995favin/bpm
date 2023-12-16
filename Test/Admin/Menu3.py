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


class Test_Admin_Menu3(unittest.TestCase):
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

    ################### admin_warehouses_check_my_tasks ###################

    def test02_admin_warehouses_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        admin = Admin_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[1]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'کالاهای سفارش', 'توضیحات بسته بندی', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[2]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'شخص ارسال کننده', 'نوع حمل', 'جمع وزن حجمی (kg)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[3]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالای سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[4]")
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'فایل های قبضی', 'آماده تحویل به مشتری', 'تاییدیه پرینت مدارک و تحویل به دلیوری'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[5]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'جزئیات', 'وزن سفارش (KG)', 'شهر مبدا', 'کالاهای ریپک'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[6]")
        my_tasks.my_tasks_check_table(11, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'توضیحات بسته بندی', 'وزن سفارش (KG)', 'پیگیری کننده'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[7]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[8]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'بارگیری کالا', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[9]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[10]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[11]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[12]")
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بارگیری کالا', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[13]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شرکت ارسال کننده', 'status', 'شماره حمل داخلی', 'کالاهای سفارش', 'وزن سفارش (KG)'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[14]")
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کل مبلغ بدهی بابت این سفارش (ریال)', 'مبلغ مازاد بر سفارش', 'توضیحات دلیوری', 'تاریخ تحویل', 'نام تحویل گیرنده', 'شماره تماس تحویل گیرنده', 'آدرس محل تحویل', 'نحوه ی پرداخت مالی سفارش جهت تحویل'])
        admin.my_tasks_check("//*[@id='task-collapse-3']/div[2]/div/div/div[2]/a[15]")
        my_tasks.my_tasks_check_table(9, ['ردیف', 'عملیات', 'ثبت هزینه و تایید نهایی', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کالاهای سفارش', 'وزن سفارش (KG)', 'شماره ترک های فرعی', 'پرداخت کننده هزینه مرجوعی'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
