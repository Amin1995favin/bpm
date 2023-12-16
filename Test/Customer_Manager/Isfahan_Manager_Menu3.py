from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Locators import *
from Pages.Customer_Manager.Tasks_List import Tasks_list
from Pages.Login import LoginPage
import unittest

# driver = webdriver.Chrome(ChromeDriverManager().install())
from selenium.webdriver.chrome.service import Service
service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


class Test_Isfahan_Manager_Menu3(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_customer_manager ###################

    def test01_login(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(isfahan_manager)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیر مشتری اصفهان شد")

    ################### customer_manager_check_my_tasks ###################

    def test02_customer_manager_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.pending_to_specify_the_sender()
        tasks_list.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'وزن سفارش (KG)'])
        tasks_list.complete_order_information()
        tasks_list.my_tasks_check_table(7, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مبلغ', 'توضیحات'])
        tasks_list.notify_customer_completion_destination_order()
        tasks_list.my_tasks_check_table(15, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شخص ارسال کننده', 'شرکت ارسال کننده', 'تلفن تماس شخص فرستنده',
                                         'تاریخ و زمان آمادگی فرستنده جهت پیک آپ',
                                         'توضیحات تاریخ و زمان آمادگی فرستنده', 'شماره ترک سفارش در شرکت حمل کننده',
                                         'نام شرکت حمل کننده', 'فایل پیوست', 'لیبل 1', 'لیبل 2', 'خروج از کارتابل'])
        tasks_list.auto_chat_by_customer()
        tasks_list.my_tasks_check_table(10,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'نام و نام خانوادگی',
                                         'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده',
                                         'تعداد سفارشات',
                                         'کارکرد مالی'])
        tasks_list.notify_order_pickup()
        sleep(1)
        tasks_list.my_tasks_check_table(6, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                            'دفعات بارگیری سفارش'])
        tasks_list.settlement_problem()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش',
                                            'ایراد تسویه', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])
        tasks_list.review_buy_requests()
        tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',
                                             'تاییدیه درخواست های خرید', 'سفارش', 'مبدا', 'مقصد', 'خدمت', 'لیست کالاها',
                                             'اطلاعات درخواست خرید', 'عملیات', 'ایجادکننده'])
        tasks_list.notify_of_buy()
        tasks_list.my_tasks_check_table(13, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل',
                                             'تاییدیه درخواست های خرید', 'سفارش', 'مبدا', 'مقصد', 'خدمت', 'لیست کالاها',
                                             'اطلاعات درخواست خرید', 'عملیات', 'ایجادکننده'])
        tasks_list.sales_claims()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'بروزرسانی',
                                            'وزن سفارش (KG)', 'خدمات موردنیاز', 'تایید مدیریت'])
    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
