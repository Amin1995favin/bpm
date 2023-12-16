from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *

from Pages.Delivery_Manager.Menu import Delivery_My_Tasks
from Pages.Clearance.Menu import My_Tasks
from Pages.Login import LoginPage
from Pages.Customer_Manager.Menu import Menu
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Delivery_Manager_Menu_Others(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_delivery_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(delivery_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر دلیوری شد. ")
        print("############################################")

    ################### delivery_manager_check_my_tasks ###################

    def test02_delivery_manager_check_my_tasks(self):
        my_tasks = My_Tasks(driver=self.driver)
        delivery = Delivery_My_Tasks(driver=self.driver)
        my_tasks.enter_clearance_my_tasks()
        my_tasks.len_clearance_my_task()
        delivery.enter_delivery_my_tasks_warehouse()
        delivery.enter_delivery_my_tasks_customer_manager1()
        delivery.receive_customer_payment_from_delivery1()
        my_tasks.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'نوع ترخیص', 'شماره بچ', 'فایل های سفارش', 'هماهنگی های انجام شده', 'تحویل دهنده', 'موزع', 'شناسه خودرو', 'نحوه تحویل کالا'])
        delivery.print_clearance_documents1()
        my_tasks.my_tasks_check_table(10, ['ردیف', 'عملیات', 'عملیات', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'بچ های سفارش', 'هماهنگی های انجام شده', 'نوع ترخیص', 'فایل های سفارش', 'علت بازگشت از آماده تحویل به مشتری'])
        delivery.receive_customer_payment_from_delivery()
        my_tasks.my_tasks_check_table(15, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'کل مبلغ بدهی بابت این سفارش (ریال)', 'مبلغ مازاد بر سفارش', 'توضیحات دلیوری', 'نوع ترخیص', 'تاریخ تحویل', 'نام تحویل گیرنده', 'شماره تماس تحویل گیرنده', 'آدرس محل تحویل', 'نحوه ی پرداخت مالی سفارش جهت تحویل', 'تحویل دهنده'])
        delivery.print_clearance_documents()
        my_tasks.my_tasks_check_table(8, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'شماره ترک فرعی', 'فایل های قبضی', 'آماده تحویل به مشتری'])
        delivery.enter_delivery_my_tasks_customer_manager()
        delivery.op_delivery_call()
        my_tasks.my_tasks_check_table(8, ['ردیف', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مشخصات وزن (KG)', 'نوع ترخیص', 'خدمات موردنیاز', 'بروزرسانی', 'مقصد سفارش'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
