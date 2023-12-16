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


class Test_Yazd_Menu2(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = driver
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    ################### Login_export ###################

    def test01_export(self):
        self.driver.get("http://testbpm.2ms.ir/login")
        login = LoginPage(driver=self.driver)
        login.enter_login_username(account_yazd)
        login.enter_login_btn_submit_next()
        login.enter_login_password(code_no_admin)
        login.enter_login_btn_submit()
        print("با موفقیت وارد پنل مدیریت شد. ")
        print("############################################")

    ################### export_check_my_tasks ###################

    def test02_export_check_my_tasks(self):
        tasks_list = Tasks_list(driver=self.driver)
        tasks_list.enter_customer_manager_my_tasks()
        tasks_list.auto_need_shipping()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'خدمات موردنیاز', 'وزن قابل پرداخت سفارش (kg)', 'ارزش کل', 'واحد ارزش'])
        tasks_list.op_delivery_call()
        sleep(1)
        tasks_list.my_tasks_check_table(10, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'مشخصات وزن (KG)', 'نوع ترخیص', 'خدمات موردنیاز', 'بروزرسانی', 'مقصد سفارش'])
        # tasks_list.flight_delay_notification_isfahan()
        # tasks_list.my_tasks_check_table(10, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'شماره ترک فرعی', 'مبدا', 'مقصد',
        #                                      'وزن سفارش (KG)', 'اطلاع رسانی به مشتری', 'خروج از کارتابل'])
        # tasks_list.check_payment_by_expert_isfahan()
        # tasks_list.my_tasks_check_table(11, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'وضعیت', 'مبلغ', 'پیش اختصاص به فاکتور ها', 'حساب', 'توضیحات', 'ایجادکننده', 'مدیر مشتری'])
        tasks_list.auto_defect_buy_information_isfahan()
        tasks_list.my_tasks_check_table(8, ['ردیف', 'عملیات', 'سفارش', 'زمان ورود وظیفه به این کارتابل', 'کالای سفارش', 'ارزش کل', 'توضیحات',
                                             'نوع پیش فاکتور خرید'])
        tasks_list.settlement_problem_isfahan()
        tasks_list.my_tasks_check_table(9, ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'سفارش', 'ایراد تسویه', 'وزن سفارش (KG)', 'خدمات موردنیاز', 'بروزرسانی'])
        tasks_list.auto_expert_customer_recovery_isfahan()
        tasks_list.my_tasks_check_table(12,
                                        ['ردیف', 'عملیات', ' ', 'زمان ورود وظیفه به این کارتابل', 'عملیات', 'نام و نام خانوادگی', 'دوره تجدید سفارش',
                                         'مدیر مشتری', 'تاریخ عضویت', 'تاریخ آخرین سفارش انجام شده', 'تعداد سفارشات',
                                         'کارکرد مالی'])

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(5)
        cls.driver.close()
        cls.driver.quit()
